from django.db import models
from django.db.models.query import QuerySet

class MealQuerySet(QuerySet):
    def public(self):
        """Filter out Meals that aren't public"""
        return self.filter(privacy="PUBLIC")

class MealManager(models.Manager):
    def get_query_set(self):
        return MealQuerySet(self.model)
    def __getattr__(self, attr, *args):
        # see https://code.djangoproject.com/ticket/15062 for details
        if attr.startswith("_"):
            raise AttributeError
        return getattr(self.get_query_set(), attr, *args)

class Meal(models.Model):
    # field definitions...
    objects = MealManager()