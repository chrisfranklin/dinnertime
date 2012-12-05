from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext as _
from userena.models import UserenaBaseProfile
from django_facebook.models import FacebookProfileModel


class UserProfile(UserenaBaseProfile, FacebookProfileModel):
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


class UserContact(models.Model):
    """
    Stores an individual contact for the users friend list
    """
    name = models.TextField(blank=True, null=True)
    user = models.ForeignKey(User, unique=True, blank=True, null=True)
    email = models.EmailField(max_length=254, blank=True, null=True)
    fid = models.BigIntegerField(blank=True, null=True)  # this should be a link to django facebook
    gender = models.CharField(choices=(
        ('F', 'female'), ('M', 'male')), blank=True, null=True, max_length=1)


from django.contrib.auth.models import User
from django.db.models.signals import post_save


def create_user_profile(sender, instance, created, **kwargs):
    """
    Creates a UserProfile when creating a User
    """
    if created:
        UserProfile.objects.create(user=instance)

post_save.connect(create_user_profile, sender=User)
