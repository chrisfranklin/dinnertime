import autocomplete_light

from accounts.models import UserContact

autocomplete_light.register(UserContact, search_fields=('search_names',),
    autocomplete_js_attributes={'placeholder': 'city name ..'})

