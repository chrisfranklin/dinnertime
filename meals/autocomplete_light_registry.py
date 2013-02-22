from meals.models import Invite, Invitee

import autocomplete_light

from django.contrib.auth.models import User
#from friends.contrib.suggest.
from accounts.models import UserContact
from meals.models import Venue


class InviteAutocomplete(autocomplete_light.AutocompleteGenericBase):
    choices = (
        User.objects.all(),
        UserContact.objects.all(),
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

    def choices_for_request(self):
        """ Return choices for a particular request """
        #user_contacts = self.choices[1]
        user = self.request.user
        print user
        contacts = self.choices[1].all()
        users = self.choices[0].all()
        contacts = contacts.filter(owner=user)
        new_choices = (users, contacts)
        self.choices = new_choices
        # for choice in user_contacts:
        #     print choice.owner
        return super(InviteAutocomplete, self).choices_for_request()

autocomplete_light.register(UserContact)
autocomplete_light.register(Invite, InviteAutocomplete)


class VenueAutocomplete(autocomplete_light.AutocompleteModelBase):
    choices = Venue.objects.all()
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

from yummly.models import Recipe


class RecipeAutocomplete(autocomplete_light.AutocompleteModelBase):
    search_fields = ('name',)


class RestAutocompleteBase(autocomplete_light. AutocompleteRestModel):
    def model_for_source_url(self, url):
        """
        Return the appropriate model for the urls defined by
        cities_light.contrib.restframework.urlpatterns.

        Used by RestChannel.
        """
        return Recipe


class RecipeRestAutocomplete(RestAutocompleteBase, RecipeAutocomplete):
    pass

ck = "9687047d"
cs = "48703203011932335cfaf5fb57ef4f1a"

autocomplete_light.register(Recipe, RecipeAutocomplete)
