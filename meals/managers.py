from django.db import models
# from django.db.models.query import QuerySet

# class MealQuerySet(QuerySet):
#     def public(self):
#         """Filter out Meals that aren't public"""
#         return self.filter(privacy="PUBLIC")

class PrivateMealManager(models.Manager):
    def get_query_set(self):
        print "HELLO!"
        # return super(PrivateMealManager, self).get_query_set().filter(privacy="PRIVATE")
