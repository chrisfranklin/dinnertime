from django.db import models

class UserProfileManager(models.Manager):
    def get_owned(self, user):
        return self.filter(owner=user)