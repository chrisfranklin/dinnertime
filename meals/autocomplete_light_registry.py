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
        'placeholder': 'type a user name ...',
    }

autocomplete_light.register(Invite, InviteAutocomplete)