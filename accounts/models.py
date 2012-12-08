from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext as _
from django_facebook.models import FacebookProfileModel


class UserProfile(FacebookProfileModel):
    """
    Stores fields for a single user, used in AUTH_PROFILE_MODULE
    """
    user = models.OneToOneField(User,
                                unique=True,
                                verbose_name=_('user'),
                                related_name='user_profile')

    def save(self, *args, **kwargs):
        # Do stuff
        super(UserProfile, self).save(*args, **kwargs)  # Call the "real" save() method.

    def __unicode__(self):
        return "Profile for " % (self.user)

    @models.permalink
    def get_absolute_url(self):
        return ('accounts_userprofile_detail', (), {'pk': self.pk})


def create_user_profile(sender, instance, created, **kwargs):
    """
    Creates a UserProfile when creating a User
    """
    if created:
        UserProfile.objects.create(user=instance)


def find_friends_suggestions(sender, instance, **kwargs):
    from friends.contrib.suggestions.models import FriendshipSuggestion
    FriendshipSuggestion.objects.create_suggestions_for_user_using_imported_contacts(instance)

from django.contrib.auth.models import User
from django.db.models.signals import post_save
post_save.connect(create_user_profile, sender=User)
post_save.connect(find_friends_suggestions, sender=User)


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
        if self.user:
            return self.user
        else:
            return self.name

    @models.permalink
    def get_absolute_url(self):
        return ('accounts_usercontact_detail', (), {'pk': self.pk})

    # We need to create a user contact every time a friend request is sent or a friend accept is done.


def create_user_contact(self, instance, **kwargs):
    """
    Create the contacts for either one side or both sides of a friendship.
    """
    print instance.from_user
    print instance.from_user
    print instance
    #print request

from friends.signals import inviting_friend, accepting_friend
inviting_friend.connect(create_user_contact)
accepting_friend.connect(create_user_contact)

#accepting_friend.send(FriendshipInvitation, request=request, invite=invitation)
