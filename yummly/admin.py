from django.contrib import admin
from .models import Recipe, Ingredient, Course, Cuisine, Allergy, Diet
#import autocomplete_light
# class MealInline(admin.StackedInline):
#     """
#     Shows meals that have been at a venue
#     """
#     model = Meal
#     extra = 0


# class UserContactAdmin(admin.ModelAdmin):
#     form = autocomplete_light.modelform_factory(UserContact)

admin.site.register(Ingredient)
admin.site.register(Recipe)
admin.site.register(Course)
admin.site.register(Cuisine)
admin.site.register(Allergy)
admin.site.register(Diet)
