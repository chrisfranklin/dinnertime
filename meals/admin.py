from django import forms
from django.contrib import admin
from easy_maps.widgets import AddressWithMapWidget
from .models import Meal, Venue, Guest, Invite, Part, MealPart


class MealInline(admin.StackedInline):
    """
    Shows meals that have been at a venue
    """
    model = Meal
    extra = 0


class VenueAdmin(admin.ModelAdmin):
    """
    Shows a venue with a maps widget for the address
    """
    inlines = [MealInline]

    class form(forms.ModelForm):

        class Meta:
            widgets = {
                'address': AddressWithMapWidget({'class': 'vTextField'})
            }


admin.site.register(Venue, VenueAdmin)
admin.site.register(Meal)
admin.site.register(MealPart)
admin.site.register(Guest)
admin.site.register(Invite)
admin.site.register(Part)
