from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext as _
from util.fields import MultiSelectField
from meals.models import Part


class UserProfile(models.Model):
    """
    Stores fields for a single user, used in AUTH_PROFILE_MODULE
    """
    user = models.OneToOneField(User,
                                unique=True,
                                verbose_name=_('user'),
                                related_name='user_profile')
    first_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    DIET_CHOICES = (
        ("MEAT", 'Meat Eater'),
        ("VEGETARIAN", 'Vegetarian'),
        ("VEGAN", 'Vegan'),
        ("PESKY", 'Pescatarian'),
        ("HALAL", "Halal"),
        ("KOSHA", "Kosha"),
    )
    diet = models.CharField(max_length=10, choices=DIET_CHOICES, default="MEAT")
    ALLERGY_CHOICES = (
        ("MILK", 'Milk'),
        ("EGGS", 'Eggs'),
        ("FISH", 'Fish'),
        ("SHELLFISH", 'Crustacean Shellfish'),
        ("TREENUTS", 'Tree Nuts'),
        ("PEANUTS", 'Peanuts'),
        ("WHEAT", 'Wheat'),
        ("SOYBEANS", 'Soybeans'),
    )
    allergies = MultiSelectField(max_length=20, blank=True, choices=ALLERGY_CHOICES)
    likes = models.ManyToManyField(Part, related_name="liked_by", blank=True, null=True)
    dislikes = models.ManyToManyField(Part, related_name="disliked_by", blank=True, null=True)

    def get_emails(self):
        """
        Returns email for a specific user, can check multiple sources for the address
        """
        # Should check allauth.account.models.EmailAddress
        # Should also check social account extra data but would be better to just import that ourselves
        return self.email

    def save(self, *args, **kwargs):
        """
        Overrides save to try and find an email address if none currently exists.
        """
        # Do stuff
        super(UserProfile, self).save(*args, **kwargs)  # Call the "real" save() method.

    def __unicode__(self):
        """
        Returns string representation of the model.
        """
        return "Profile for " % (self.user)

    @models.permalink
    def get_absolute_url(self):
        """
        Returns a URL for the specific object
        """
        return ('accounts_userprofile_detail', (), {'pk': self.pk})


def create_user_profile(sender, instance, created, **kwargs):
    """
    Creates a UserProfile when creating a User
    """
    if created:
        UserProfile.objects.create(user=instance)


def find_friends_suggestions(sender, instance, **kwargs):
    """
    Checks imported contacts for a specific user to see if we can create any friend suggestions
    """
    from friends.contrib.suggestions.models import FriendshipSuggestion
    FriendshipSuggestion.objects.create_suggestions_for_user_using_imported_contacts(instance)

from django.contrib.auth.models import User
from django.db.models.signals import post_save
post_save.connect(create_user_profile, sender=User)
#post_save.connect(find_friends_suggestions, sender=User)

from django.dispatch import receiver
from rest_framework.authtoken.models import Token

@receiver(post_save, sender=User)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        pass
        #Token.objects.create(user=instance)


class UserContactManager(models.Manager):
    def get_query_set(self):
        print "HELLO!"
        return super(UserContactManager, self).get_query_set().filter(privacy="PRIVATE")


class UserContact(models.Model):
    """
    Stores an individual contact for the users friend list
    """
    # user who imported this contact
    owner = models.ForeignKey(User, verbose_name=_("owner"), related_name="contacts")
    name = models.TextField(blank=True, null=True)
    user = models.ForeignKey(User, unique=True, blank=True, null=True)
    email = models.EmailField(max_length=254, blank=True, null=True)
    fid = models.BigIntegerField(blank=True, null=True)  # this should be a link to django facebook
    gender = models.CharField(choices=(
        ('F', 'female'), ('M', 'male')), blank=True, null=True, max_length=1)

    def __unicode__(self):
        """
        Returns string representation of the model.
        """
        return self.name

    @models.permalink
    def get_absolute_url(self):
        """
        Returns a URL for the specific object
        """
        return ('accounts_usercontact_detail', (), {'pk': self.pk})

    def save(self, *args, **kwargs):
        """
        Overrides save to try and find an email address if none currently exists.
        """
        # Do stuff
        if not self.email:
            # We don't have an email, lets check emails and allauth
            if self.user:
                # We have a user
                if self.user.email:
                    # It has an email
                    self.email = self.user.email
        super(UserContact, self).save(*args, **kwargs)  # Call the "real" save() method.

    # We need to create a user contact every time a friend request is sent or a friend accept is done.

# ================================================================================================================================
# The following code will be useful if we decide to make the contacts
# search only return friends rather than all users of the site

# def create_user_contact(self, instance, **kwargs):
#     """
#     Creates the contacts for either one side or both sides of a friendship.
#     """
#     print instance.from_user
#     print instance.from_user
#     print instance
#     #print request

# from friends.signals import inviting_friend, accepting_friend
# inviting_friend.connect(create_user_contact)
# accepting_friend.connect(create_user_contact)

# accepting_friend.send(FriendshipInvitation, request=request, invite=invitation)
