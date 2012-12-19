from django.db import models
from jsonfield import JSONField


class Ingredient(models.Model):
    """
    Stores an ingredient from the yummly metadata api
    """
    remote_id = models.CharField(max_length=50, blank=True, null=True)
    ingredient_id = models.CharField(max_length=50, blank=True, null=True)
    search_value = models.CharField(max_length=50, blank=True, null=True)
    term = models.CharField(max_length=50, blank=True, null=True)
    use_count = models.CharField(max_length=50, blank=True, null=True)

    def __unicode__(self):
        return unicode(self.term)


class Allergy(models.Model):
    """
    Stores allergy type from the yummly metadata api
    """
    remote_id = models.CharField(max_length=50, blank=True, null=True)
    description = models.CharField(max_length=50, blank=True, null=True)
    search_value = models.CharField(max_length=50, blank=True, null=True)

    def __unicode__(self):
        return self.description


class Diet(models.Model):
    """
    Stores a diet type from the yummly metadata api
    """
    remote_id = models.CharField(max_length=50, blank=True, null=True)
    description = models.CharField(max_length=50, blank=True, null=True)
    search_value = models.CharField(max_length=50, blank=True, null=True)

    def __unicode__(self):
        return self.description


class Course(models.Model):
    """
    Stores a course type from the yummly metadata api
    """
    remote_id = models.CharField(max_length=50, blank=True, null=True)
    description = models.CharField(max_length=50, blank=True, null=True)
    search_value = models.CharField(max_length=50, blank=True, null=True)

    def __unicode__(self):
        return self.description


class Cuisine(models.Model):
    """
    Stores a cuisine type from the yummly metadata api
    """
    remote_id = models.CharField(max_length=50, blank=True, null=True)
    description = models.CharField(max_length=50, blank=True, null=True)
    search_value = models.CharField(max_length=50, blank=True, null=True)

    def __unicode__(self):
        return self.description


class Recipe(models.Model):
    """
    Stores a recipe from the yummly recipe api
    """
    flavors = models.CharField(max_length=50, blank=True, null=True)
    remote_id = models.CharField(max_length=50, blank=True, null=True)
    ingredients = models.ManyToManyField(Ingredient, blank=True, null=True)
    rating = models.CharField(max_length=50, blank=True, null=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    small_image_urls = JSONField(blank=True, null=True)
    source_display_name = models.CharField(max_length=50, blank=True, null=True)
    total_time_in_seconds = models.IntegerField(blank=True, null=True)
    course = models.ForeignKey(Course, blank=True, null=True)  # get from attributes

    # DIET_CHOICES = (
    #     ("MEAT", 'Meat Eater'),
    #     ("VEGETARIAN", 'Vegetarian'),
    #     ("VEGAN", 'Vegan'),
    #     ("PESKY", 'Pescatarian'),
    #     ("HALAL", "Halal"),
    #     ("KOSHA", "Kosha"),
    # )
    # diet = models.CharField(max_length=10, choices=DIET_CHOICES, default="MEAT")

    # def save(self, *args, **kwargs):
    #     # Do stuff
    #     super(UserProfile, self).save(*args, **kwargs)  # Call the "real" save() method.

    def __unicode__(self):
        return self.name

    # @models.permalink
    # def get_absolute_url(self):
    #     return ('accounts_userprofile_detail', (), {'pk': self.pk})
