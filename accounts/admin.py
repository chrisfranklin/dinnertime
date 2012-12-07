from django.contrib import admin
from .models import UserProfile, UserContact

# class MealInline(admin.StackedInline):
#     """
#     Shows meals that have been at a venue
#     """
#     model = Meal
#     extra = 0


# class VenueAdmin(admin.ModelAdmin):
#     """
#     Shows a venue with a maps widget for the address
#     """
#     inlines = [MealInline]

#     class form(forms.ModelForm):

#         class Meta:
#             widgets = {
#                 'address': AddressWithMapWidget({'class': 'vTextField'})
#             }


#admin.site.register(Venue, VenueAdmin)
admin.site.register(UserProfile)
admin.site.register(UserContact)

