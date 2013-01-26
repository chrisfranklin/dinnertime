from meals.models import Invite, Invitee

import autocomplete_light

from django.contrib.auth.models import User
#from friends.contrib.suggest.
from accounts.models import UserContact
from meals.models import Venue

class InviteAutocomplete(autocomplete_light.AutocompleteGenericBase):
    choices = (
        User.objects.all(),
        UserContact.objects.filter(),
    )
    search_fields = (
        ('username', 'email', 'first_name', 'last_name'),
        ('name', 'email'),
    )
    # optionnal: override a widget.js option
    widget_js_attributes = {
        'max_values': 3,
        'data-bootstrap': 'yourinit',
        }
    def choice_value(self, choice):
        return choice.email
    # Note that defining *_js_attributes in a Widget also works. Widget has
    # priority since it's the most specific.
    autocomplete_js_attributes = {
        'placeholder': 'enter name or email',
    }

    # def choices_for_request(self):
    #     """ Return choices for a particular request """
    #     print self
    #     return super(InviteAutocomplete, self).choices_for_request(
    #         ).exclude(extra=self.request.GET['extra'])

autocomplete_light.register(UserContact)
autocomplete_light.register(Invite, InviteAutocomplete)


class VenueAutocomplete(autocomplete_light.AutocompleteModelBase):
    choices = Venue
    search_fields = ('address', 'name')
    # optionnal: override a widget.js option
    widget_js_attributes = {
        'max_values': 3,
        }

    def choice_value(self, choice):
        return choice.address
    # Note that defining *_js_attributes in a Widget also works. Widget has
    # priority since it's the most specific.
    autocomplete_js_attributes = {
        'placeholder': 'enter location or name',
    }

    # def choices_for_request(self):
    #     """ Return choices for a particular request """
    #     print self
    #     return super(InviteAutocomplete, self).choices_for_request(
    #         ).exclude(extra=self.request.GET['extra'])

autocomplete_light.register(Venue, VenueAutocomplete)
