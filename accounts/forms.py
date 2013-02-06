from django import forms

import autocomplete_light

from models import UserContact

# in the case of this example, we could just have:
# UserContactForm = autocomplete_light.modelform_factory(UserContact)
# but we'll not use this shortcut


class UserContactForm(forms.ModelForm):
    """
    Provides form for user contact model with autocomplete widget.
    """
    class Meta:
        widgets = autocomplete_light.get_UserContacts_dict(UserContact)
        model = UserContact
