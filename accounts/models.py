from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext as _
from userena.models import UserenaBaseProfile

class UserProfile(UserenaBaseProfile):
    user = models.OneToOneField(User,
                                unique=True,
                                verbose_name=_('user'),
                                related_name='user_profile')


    def save(self, *args, **kwargs):
        # Do stuff
        super(UserProfile, self).save(*args, **kwargs) # Call the "real" save() method.


    def __unicode__(self):
        return "Profile for " % (self.user)



from django.contrib.auth.models import User
from django.db.models.signals import post_save


#Make sure we create a UserProfile when creating a User
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

post_save.connect(create_user_profile, sender=User)