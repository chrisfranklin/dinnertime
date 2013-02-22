from django.db import models
from jsonfield import JSONField


class Ingredient(models.Model):
    """
    Stores an ingredient from the yummly metadata api
    """
    remote_id = models.CharField(max_length=200, blank=True, null=True)
    ingredient_id = models.CharField(max_length=200, blank=True, null=True)
    search_value = models.CharField(max_length=200, blank=True, null=True)
    term = models.CharField(max_length=200, blank=True, null=True)
    use_count = models.CharField(max_length=200, blank=True, null=True)

    def __unicode__(self):
        return unicode(self.term)


class Allergy(models.Model):
    """
    Stores allergy type from the yummly metadata api
    """
    remote_id = models.CharField(max_length=200, blank=True, null=True)
    description = models.CharField(max_length=200, blank=True, null=True)
    search_value = models.CharField(max_length=200, blank=True, null=True)

    def __unicode__(self):
        return self.description


class Diet(models.Model):
    """
    Stores a diet type from the yummly metadata api
    """
    remote_id = models.CharField(max_length=200, blank=True, null=True)
    description = models.CharField(max_length=200, blank=True, null=True)
    search_value = models.CharField(max_length=200, blank=True, null=True)

    def __unicode__(self):
        return self.description


class Course(models.Model):
    """
    Stores a course type from the yummly metadata api
    """
    remote_id = models.CharField(max_length=200, blank=True, null=True)
    description = models.CharField(max_length=200, blank=True, null=True)
    search_value = models.CharField(max_length=200, blank=True, null=True)

    def __unicode__(self):
        return self.description


class Cuisine(models.Model):
    """
    Stores a cuisine type from the yummly metadata api
    """
    remote_id = models.CharField(max_length=200, blank=True, null=True)
    description = models.CharField(max_length=200, blank=True, null=True)
    search_value = models.CharField(max_length=200, blank=True, null=True)

    def __unicode__(self):
        return self.description

class Flavor(models.Model):
    bitter = models.DecimalField(max_digits=28, decimal_places=25)
    meaty = models.DecimalField(max_digits=28, decimal_places=25)
    piquant = models.DecimalField(max_digits=28, decimal_places=25)
    salty = models.DecimalField(max_digits=28, decimal_places=25)
    sour = models.DecimalField(max_digits=28, decimal_places=25)
    sweet = models.DecimalField(max_digits=28, decimal_places=25)

class Recipe(models.Model):
    """
    Stores a recipe from the yummly recipe api
    """
    flavor = models.ForeignKey(Flavor, blank=True, null=True)
    remote_id = models.CharField(max_length=200, blank=True, null=True)
    ingredients = models.ManyToManyField(Ingredient, blank=True, null=True)
    rating = models.CharField(max_length=200, blank=True, null=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    small_image_urls = JSONField(blank=True, null=True)
    large_image_urls = JSONField(blank=True, null=True)
    source_display_name = models.CharField(max_length=200, blank=True, null=True)
    total_time_in_seconds = models.IntegerField(blank=True, null=True)
    course = models.ManyToManyField(Course, blank=True, null=True)  # get from attributes

    def small_image(self):
        if self.small_image_urls:
            return self.small_image_urls[0]

    def large_image(self):
        if self.large_image_urls:
            return self.large_image_urls[0]

    def total_time_in_minutes(self):
        return self.total_time_in_seconds / 60

    def total_time_in_hours(self):
        return self.total_time_in_minutes / 60

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
        if self.name:
            return unicode(self.name)
        else:
            return "recipe"

    # @models.permalink
    # def get_absolute_url(self):
    #     return ('accounts_userprofile_detail', (), {'pk': self.pk})
