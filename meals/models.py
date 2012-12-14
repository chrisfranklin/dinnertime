from django.db import models
from django.contrib.auth.models import User
#from jsonfield import JSONField
from actstream import action


class Venue(models.Model):
    """
    Stores the location of a meal, can be used multiple times, tied to user model.
    """
    name = models.CharField(max_length=50)
    address = models.TextField(blank=True, null=True)
    user = models.ForeignKey(User)

    def __unicode__(self):
        return self.name

    @models.permalink
    def get_absolute_url(self):
        return ('meals_venue_detail', (), {'pk': self.pk})


class Part(models.Model):
    STATUS_CHOICES = (
        ("WANT", 'I want'),
        ("NEED", 'I need'),
        ("HAVE", 'I have'),
    )
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    fulfilled_by = models.ForeignKey(User, blank=True, null=True)
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name

    @models.permalink
    def get_absolute_url(self):
        return ('meals_part_detail', (), {'pk': self.pk})


class Meal(models.Model):
    """
    Stores an instance of a meal
    """
    name = models.CharField(max_length=120, blank=True, null=True)
    host = models.ForeignKey(User, related_name="hosted")
    when = models.DateTimeField()
    icon = models.ImageField(upload_to="meal/icon/", blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    venue = models.ForeignKey(Venue, blank=True, null=True)
    max_guests = models.IntegerField(default=4)
    current_guests = models.IntegerField(default=0)
    guests = models.ManyToManyField(User, related_name="attended", through='Guest', blank=True, null=True)
    SUITABLE_FOR_CHOICES = (
        ("MEAT", 'Meat Eaters'),
        ("VEGETARIAN", 'Vegetarians'),
        ("VEGAN", 'Vegans'),
    )
    suitable_for = models.CharField(max_length=10, choices=SUITABLE_FOR_CHOICES, default="MEAT")
    PRIVACY_CHOICES = (
        ("PRIVATE", 'Invite Only'),
        ("PUBLIC", 'Public'),
    )
    privacy = models.CharField(max_length=10, choices=PRIVACY_CHOICES, default="PRIVATE")
    parts = models.ManyToManyField(Part, blank=True, null=True)
    #cut off for rsvp needs adding
    #recipe

    def save(self, *args, **kwargs):
        """
        Overrides save to provide notification on meal changes
        """
        
        super(Meal, self).save(*args, **kwargs)  # Call the "real" save() method.

    def add_guest(self, guest, invite, plusone=0):
        """
        Increments current_guests if not greater than max_guests and returns true else returns false
        """
        if self.max_guests >= self.current_guests + plusone:
            # We have room at the meal for the person and their plusones
            self.current_guests += plusone + 1  # The extra one is for the actual guest
            self.save()
            guest_model = Guest(user=guest, meal=self, invite=invite)
            guest_model.save()
            print guest_model
            return True
        else:
            # We do not have room for the person and their plusones
            return False

    def remove_guest(self, guest):
        pass

    def increase_max_guests(self):
        """
        Increments max_guests and returns true else returns false
        """
        self.max_guests += 1
        self.save()
        return True

    def decrease_max_guests(self):
        """
        Decrements max_guests if the meal is not already full and returns true else returns false
        """
        if self.max_guests > self.current_guests and self.max_guests > 0:
            # We have room at the meal even after decrementing max guests so lets do it.
            self.max_guests -= 1
            self.save()
            return True
        else:
            # The meal is full, remove some guests before decreasing the size.
            return False

    def share_to_facebook(self, graph=None, **kwargs):
        """
        Stores and tries sending a facebook open graph share of the meal.
        """
        from django_facebook.models import OpenGraphShare
        #this is where the magic happens
        share = OpenGraphShare.objects.create(
            user_id=self.user_id,
            action_domain='fashiolista:love',
            #content_type=content_type,
            object_id=self.id,
        )
        share.set_share_dict(kwargs)
        share.save()
        return share.send()

    def __unicode__(self):
        return "%s meal" % (self.host)

    @models.permalink
    def get_absolute_url(self):
        return ('meals_meal_detail', (), {'pk': self.pk})

from accounts.models import UserContact


class Invite(models.Model):
    """
    Stores an individual invite to a meal, converts invite to guest with correct secret.
    """
    meal = models.ForeignKey(Meal)
    secret = models.CharField(max_length=50, blank=True, null=True)
    contact = models.ForeignKey(UserContact, blank=True, null=True)
    STATUS_CHOICES = (
        ("INVITED", 'Invited'),
        ("ACCEPTED", 'Accepted'),
        ("CANCELLED", 'Cancelled'),
        ("DECLINED", 'Declined'),
    )
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="INVITED")
    plusones = models.IntegerField(default=0)
    max_plusones = models.IntegerField(default=1, blank=True, null=True)
    single_use = models.BooleanField(default=True)

    invited_by = models.ForeignKey(User, blank=True, null=True)

    @models.permalink
    def get_absolute_url(self):
        return ('meals_invite_detail', (), {'pk': self.pk})

    def send_invite(self):
        """
        Sends the invite via any available communications channel
        """
        if self.contact:
            # Send Meal invite to the contact
            self.contact.send_invite(self)
        else:
            # We should never get here
            print "No contact for invite #%s" % self.id

    def accept_invite(self, secret, user):
        """
        Checks a secret and allows an invitee to become a guest if it is valid and they are logged in somehow.
        """
        if self.check_secret(secret):
            # Secret matches
            if self.status == "INVITED" or not self.single_use:
                # If the code is not used or can be used multiple times then continue.
                # If the user has an email or a facebook we should try and match it to a profile perhaps.
                if user:
                    # We have a user
                    print user
                    if self.meal.add_guest(user, self, self.plusones):
                        # We have allocated the space at the table
                        # Set status to accepted
                        self.status = "ACCEPTED"
                        self.save()
                        action.send(self.contact, verb='accepted invite to', action_object=self.meal)
                        # We should save any other info we have about the user to the user profile for display
                    else:
                        # There is not space at the table, we could try with less plusones in future
                        pass
                else:
                    # No user (not even a lazy one!)
                    pass
        else:
            # The secret doesn't match
            print("Bad secret")
            print self.secret
            print secret
        pass

    def decline_invite(self, secret):
        """
        Changes invite status to declined
        """
        if self.single_use:
            self.status = "DECLINED"
            action.send(self.contact, verb='declined invite to', action_object=self.meal)

    def cancel_invite(self, secret):
        """
        Removes user from meal guests list
        """
        pass

    def create_guest(self, user):
        """
        Stores a guest instance from a user and the current meal
        """
        # We should check that max_guests isn't already reached.
        guest = Guest(user=user, meal=self.meal)
        return guest.save()

    def generate_secret(self):
        """
        Creates a unique identifier for the invite and saves it.
        """
        if hasattr(self, 'meal'):
            import hashlib
            from util.misc import get_random_string
            salt = get_random_string()
            secret = hashlib.sha1(salt + str(self.meal)).hexdigest()
            return secret
        else:
            return None

    def check_secret(self, secret):
        """
        Checks if a secret is valid
        """
        return self.secret == secret

    def send_email(self):
        """
        Sends an email if we have one available
        """
        print "wanknut"
        if self.contact.email:
            # Nice and easy we have an email on the contact, also check for allauth and for one on the user
            from django.core.mail import send_mail
            send_mail('You have been invited to a meal', 'Test message http://localhost:8000/meal/%s/invite/%s/y/%s/' % (self.meal.id, self.pk, self.secret), 'dt@piemonster.me', [self.contact.email], fail_silently=False)

    def save(self, *args, **kwargs):
        """
        Overrides save to generate a secret if their isn't one
        """
        if not self.secret:
            self.secret = self.generate_secret()
        if self.id is None:
            self.send_email()
            action.send(self.contact, verb='was invited to', action_object=self.meal)
        super(Invite, self).save(*args, **kwargs)  # Call the "real" save() method.


class Guest(models.Model):
    """
    Stores an individual guest for a meal, junction tables for meal.guests
    """
    user = models.ForeignKey(User)
    meal = models.ForeignKey(Meal)
    invite = models.ForeignKey(Invite)
    parts = models.ManyToManyField(Part, blank=True, null=True)
    # TODO: Add something for allergies and *isms
