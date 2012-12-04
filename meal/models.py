from django.db import models
from django.contrib.auth.models import User
from jsonfield import JSONField


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
        return ('meal_venue_detail', (), {'pk': self.pk})


class Meal(models.Model):
    """
    Stores an instance of a meal
    """
    host = models.ForeignKey(User, related_name="hosted")
    when = models.DateTimeField()
    icon = models.ImageField(upload_to="meal/icon/", blank=True, null=True)
    description = models.TextField()
    venue = models.ForeignKey(Venue)
    max_guests = models.IntegerField()
    guests = models.ManyToManyField(User, related_name="attended", through='Guest')
    SUITABLE_FOR_CHOICES = (
        ("MEAT", 'Meat Eaters'),
        ("VEGETARIAN", 'Vegetarians'),
        ("VEGAN", 'Vegans'),
    )
    suitable_for = models.CharField(max_length=10, choices=SUITABLE_FOR_CHOICES, default="MEAT")
    wants = JSONField()
    needs = JSONField()
    haves = JSONField()  
    # seats and cut off for rsvp need adding
    #recipe
    

    def __unicode__(self):
        return "%s meal" % (self.host)

    @models.permalink
    def get_absolute_url(self):
        return ('meal_meal_detail', (), {'pk': self.pk})


class Guest(models.Model):
    """
    Stores an individual guest for a meal, junction tables for meal.guests
    """
    user = models.ForeignKey(User)
    meal = models.ForeignKey(Meal)
