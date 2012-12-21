from meals.models import Invite

import autocomplete_light

from django.contrib.auth.models import User
#from friends.contrib.suggest.
from accounts.models import UserContact

class InviteAutocomplete(autocomplete_light.AutocompleteGenericBase):
    choices = (
        User.objects.all(),
        UserContact.objects.all(),
    )
    search_fields = (
        ('username', 'email', 'first_name', 'last_name'),
        ('name', 'email'),
    )

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

autocomplete_light.register(Invite, InviteAutocomplete)