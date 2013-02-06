from django.db import models

class UserProfileManager(models.Manager):
	"""
    Provides a custom manager for UserProfile objects
    """
    def get_owned(self, user):
        return self.filter(owner=user)

class UserContactManager(models.Manager):
	"""
    Provides a custom manager for UserContact objects
    """
    def get_owned(self, user):
    	"""
	    Returns objects that are owned by the specified user
	    """
        return self.filter(owner=user)