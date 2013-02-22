from django.db import models


class UserContactManager(models.Manager):
    """
    Provides custom manager for user contact objects
    """
    def get_owned(self, user):
        return self.filter(owner=user)
