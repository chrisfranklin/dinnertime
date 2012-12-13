from django.contrib import admin
from .models import UserProfile, UserContact
import autocomplete_light
# class MealInline(admin.StackedInline):
#     """
#     Shows meals that have been at a venue
#     """
#     model = Meal
#     extra = 0


class UserContactAdmin(admin.ModelAdmin):
    form = autocomplete_light.modelform_factory(UserContact)

admin.site.register(UserProfile)
admin.site.register(UserContact, UserContactAdmin)
