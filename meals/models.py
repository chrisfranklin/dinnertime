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
    """
    Stores a have, need or want as a part.
    """
    TYPE_CHOICES = (
        ("FURNITURE", 'Furniture'),
        ("EQUIPMENT", 'Equipment'),
        ("INGREDIENT", 'Ingredient'),
        ("BEVERAGE", 'Beverage'),
        ("DISH", 'Dish'),
    )
    part_type = models.CharField(max_length=18, choices=TYPE_CHOICES)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=50, blank=True, null=True)
    unit = models.CharField(max_length=30, blank=True, null=True)

    def __unicode__(self):
        return self.name

    @models.permalink
    def get_absolute_url(self):
        return ('meals_part_detail', (), {'pk': self.pk})

from yummly.models import Recipe


class Meal(models.Model):
    """
    Stores an instance of a meal, very important model.
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
    parts = models.ManyToManyField(Part, blank=True, null=True, through='MealPart')
    #cut off for rsvp needs adding
    recipe = models.ForeignKey(Recipe, blank=True, null=True)

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
            action.send(guest, verb='is attending', action_object=self)
            print guest_model
            return True
        else:
            # We do not have room for the person and their plusones
            return False

    def add_have(self, name, user, **kwargs):
        """
        Represents a "have" part of the meal with the relevant item_type populated from add_type() and kwargs
        """
        part = Part.objects.get_or_create(name=name)[0]
        meal_part, created = MealPart.objects.get_or_create(meal=self, part=part, status="HAVE")
        if created:
            meal_part.added_by = user
            meal_part.save()
        return meal_part

    def add_need(self, name, user, **kwargs):
        """
        Represents a "need" part of the meal with the relevant item_type populated from add_type() and kwargs
        """
        part = Part.objects.get_or_create(name=name)[0]
        meal_part, created = MealPart.objects.get_or_create(meal=self, part=part, status="NEED")
        if created:
            meal_part.added_by = user
            meal_part.save()
        return meal_part

    def add_want(self, name, user, **kwargs):
        """
        Represents a "want" part of the meal with the relevant item_type populated from add_type() and kwargs
        """
        part = Part.objects.get_or_create(name=name)[0]
        meal_part, created = MealPart.objects.get_or_create(meal=self, part=part, status="WANT")
        if created:
            meal_part.added_by = user
            meal_part.save()
        return meal_part

    def remove_guest(self, guest):
        pass

    def increase_max_guests(self):
        """
        Increments max_guests and returns true else returns false
        """
        self.max_guests += 1
        self.save()
        action.send(self.host, verb='increased max guests for', action_object=self)
        return True

    def decrease_max_guests(self):
        """
        Decrements max_guests if the meal is not already full and returns true else returns false
        """
        if self.max_guests > self.current_guests and self.max_guests > 0:
            # We have room at the meal even after decrementing max guests so lets do it.
            self.max_guests -= 1
            self.save()
            action.send(self.host, verb='decreased max guests for', action_object=self)
            return True
        else:
            # The meal is full, remove some guests before decreasing the size.
            return False

    def __unicode__(self):
        return "%s meal" % (self.host)

    @models.permalink
    def get_absolute_url(self):
        return ('meals_meal_detail', (), {'pk': self.pk})


class MealPart(models.Model):
    """
    Stores an individual part for a meal, junction table for meal.parts
    """
    part = models.ForeignKey(Part)
    meal = models.ForeignKey(Meal)
    STATUS_CHOICES = (
        ("WANT", 'I want'),
        ("NEED", 'I need'),
        ("HAVE", 'I have'),
    )
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, blank=True, null=True)
    quantity = models.IntegerField(blank=True, null=True)
    added_by = models.ForeignKey(User, blank=True, null=True, related_name="requested")
    fulfilled_by = models.ForeignKey(User, blank=True, null=True, related_name="fulfilled")


class Invitee(models.Model):
    """
    Stores contact details for an individual invitee
    """
    name = models.CharField(max_length=50, blank=True, null=True)
    user = models.ForeignKey(User, unique=True, blank=True, null=True)
    email = models.EmailField(max_length=254, blank=True, null=True)

    def get_avatar(self):
        return self.email

    def get_email(self):
        if self.email:
            return self.email
        elif self.user:
            if self.user.email:
                return self.user.email
        else:
            return "No email or error!"

    def save(self, *args, **kwargs):
        """
        Overrides save to tie to a user if one exists for the email.
        """
        if self.id is None:
            # The invitee has just been created, lets see if we have a user
            if self.user:
                # we do have a user with that email address, we should get the name if its not set
                if self.name:
                    pass  # we already have a name
                else:
                    self.name = str(self.user)  # set invitee name to username
                pass
            else:
                # We do not have a user set already, let's see if any match our requirements
                from accounts.models import UserProfile
                try:
                    self.user = UserProfile.objects.get(user__email=self.email).user
                except:
                    print "No user :("
                    pass
        super(Invitee, self).save(*args, **kwargs)  # Call the "real" save() method.


class Invite(models.Model):
    """
    Stores an individual invite to a meal, converts invite to guest with correct secret.
    """
    meal = models.ForeignKey(Meal)
    secret = models.CharField(max_length=50, blank=True, null=True)
    invitee = models.ForeignKey(Invitee, blank=True, null=True)
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

    invited_by = models.ForeignKey(User, blank=True, null=True, related_name="invited_by")

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

    def send_email(self, from_email):
        """
        Sends an email if we have one available
        """
        print "wanknut"
        # here we should check if we have a user and if we do then use the users preferred method of contact.
        if self.invitee.email:
            # Nice and easy we have an email on the contact, also check for allauth and for one on the user
            to_email = self.invitee.email
            from django.core.mail import send_mail
            send_mail('You have been invited to a meal', 'Test http://localhost:8000/meal/%s/invite/y/%s/' % (self.meal.id, self.secret), from_email, [to_email], fail_silently=False)
        else:
            print "No email has been found!"

    def save(self, *args, **kwargs):
        """
        Overrides save to generate a secret if their isn't one
        """
        if not self.secret:
            self.secret = self.generate_secret()
        if self.id is None:
            # The invite has just been created, lets see if we have a user
            if self.invited_by:
                from_email = self.invited_by.email
            else:
                from_email = "chris@piemonster.me"
            self.send_email(from_email)
            action.send(self.invitee, verb='was invited to', action_object=self.meal)
        super(Invite, self).save(*args, **kwargs)  # Call the "real" save() method.


class Guest(models.Model):
    """
    Stores an individual guest for a meal, junction tables for meal.guests
    """
    user = models.ForeignKey(User)
    meal = models.ForeignKey(Meal)
    invite = models.ForeignKey(Invite)
    # TODO: Add something for allergies and *isms
