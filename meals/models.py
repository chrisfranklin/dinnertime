from django.db import models
from django.contrib.auth.models import User
from jsonfield import JSONField


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


class Meal(models.Model):
    """
    Stores an instance of a meal
    """
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
        ("PRIVATE", 'Private'),
        ("PUBLIC", 'Public'),
    )
    privacy = models.CharField(max_length=10, choices=PRIVACY_CHOICES, default="PRIVATE")
    wants = JSONField(blank=True, null=True)
    needs = JSONField(blank=True, null=True)
    haves = JSONField(blank=True, null=True)
    #cut off for rsvp needs adding
    #recipe

    def add_guest(self, plusone=0):
        if self.max_guests > self.current_guests + plusone:
            # We have room at the meal for the person and their plusones
            self.current_guests += plusone + 1  # The extra one is for the actual guest
            return True
        else:
            # We do not have room for the person and their plusones
            return False

    def share_to_facebook(self, graph=None, **kwargs):
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
        return ('meal_meal_detail', (), {'pk': self.pk})


class Invite(models.Model):
    """
    Stores an individual invite to a meal, converts invite to guest with correct secret.
    """
    meal = models.ForeignKey(Meal)
    secret = models.CharField(max_length=50, blank=True, null=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    STATUS_CHOICES = (
        ("INVITED", 'Invited'),
        ("ACCEPTED", 'Accepted'),
    )
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="INVITED")
    email = models.EmailField(max_length=254, blank=True, null=True)
    fid = models.CharField(max_length=30, blank=True, null=True)
    plusones = models.IntegerField(default=0)
    max_plusones = models.IntegerField(default=1)

    def send_invite(self):
        if self.fid:
            # Send Facebook invite to user
            pass
        if self.email:
            # Send Email invite to user
            pass

    def accept_invite(self, secret, user):
        if self.check_secret(secret):
            # Secret matches
            # If the user has an email or a facebook we should try and match it to a profile perhaps.
            if user:
                # We have a user
                if self.meal.add_guest(self.plusones):
                    # We have allocated the space at the table
                    self.create_guest(user)
                    # Set status to accepted, we should really check if the guest was created
                    self.status = "ACCEPTED"
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
        pass

    def create_guest(self, user):
        # We should check that max_guests isn't already reached.
        guest = Guest(user=user, meal=self.meal)
        guest.save()

    def generate_secret(self):
        import hashlib
        from util.misc import get_random_string
        salt = get_random_string()
        secret = hashlib.sha1(salt + str(self.meal)).hexdigest()
        return secret

    def check_secret(self, secret):
        return self.secret == secret

    def save(self):
        self.secret = self.generate_secret()
        super(Invite, self).save()  # Call the "real" save() method.


class Guest(models.Model):
    """
    Stores an individual guest for a meal, junction tables for meal.guests
    """
    user = models.ForeignKey(User)
    meal = models.ForeignKey(Meal)
