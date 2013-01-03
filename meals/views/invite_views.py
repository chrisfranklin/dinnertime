from django.views.generic import ListView, DetailView, CreateView, \
                                 DeleteView, UpdateView


from meals.models import Invite, Meal

from accounts.models import UserContact
from django.http import HttpResponseRedirect


class InviteView(object):
    model = Invite

    def get_template_names(self):
        """Nest templates within invite directory."""
        tpl = super(InviteView, self).get_template_names()[0]
        app = self.model._meta.app_label
        mdl = 'invite'
        self.template_name = tpl.replace(app, '{0}/{1}'.format(app, mdl))
        return [self.template_name]


class InviteBaseListView(InviteView):
    paginate_by = 10


from django import forms
import autocomplete_light


class UserContactAutocomplete(autocomplete_light.AutocompleteModelBase):
    search_fields = ('name', 'email')

    # Note that defining *_js_attributes in a Widget also works. Widget has
    # priority since it's the most specific.
    autocomplete_js_attributes = {
        'placeholder': 'type a user name ...',
    }


autocomplete_light.register(UserContact, UserContactAutocomplete)

from django.contrib.auth.models import User


class InviteForm(forms.ModelForm):
    choices = (
        User.objects.all(),
    )
    #user = forms.ModelChoiceField(User.objects.all(),
    #    widget=autocomplete_light.ChoiceWidget('UserAutocomplete'))

    email = forms.CharField(widget=autocomplete_light.TextWidget('InviteAutocomplete'))
    #email = forms.ModelChoiceField(UserContact.objects.all(), widget=autocomplete_light.TextWidget('InviteAutocomplete'))

    # Note that defining *_js_attributes on Autocomplete classes or instances
    # also work.

    class Meta:
        model = Invite
        exclude = ('secret', 'plusones', 'status', 'single_use', 'meal', 'invited_by', 'user')



from django.shortcuts import render_to_response
from django.template import RequestContext

from django.template.loader import render_to_string
#from django.views.decorators.http import require_POST


def _invite_data(request, invite):
    data = {
        "html": render_to_string(
            "_invite.html",
            RequestContext(request, {
                "invite": invite
            })
        )
    }
    return data

#from django.http import HttpResponse
#import json


def add_invite(request, meal_id):
    if request.method == "POST":
        form = InviteForm(request.POST, request.FILES)
        if form.is_valid():
            meal = Meal.objects.get(pk=meal_id)
            email = form.cleaned_data['email']
            # we have a valid email address, we should check if we have a user with that email and add that too maybe. 
            user = User.objects.get(email=email)
            print user
            max_plusones = form.cleaned_data['max_plusones']
            invite = Invite.objects.get_or_create(email=email, max_plusones=max_plusones, meal=meal, user=user)[0]
            #data = _invite_data(request, invite)
            #return HttpResponseRedirect(invite.meal.get_absolute_url())
            return HttpResponseRedirect(meal.get_absolute_url())
    else:
        form = InviteForm()
    return render_to_response("meals/meal/invite/invite_form.html", {'form': form}, context_instance=RequestContext(request))


def ack_invite(request, meal_id, action, secret):
    #meal = Meal.objects.get(pk=meal_id)
    invite = Invite.objects.get(secret=secret, meal=meal_id)  # Add error checking to shrug off invalid invites
    if action == "y":
        print "gotcha"
        print request.user
        invite.accept_invite(secret, request.user)
        return HttpResponseRedirect(invite.meal.get_absolute_url())
    elif action == "n":
        invite.decline_invite(None, None)
        return HttpResponseRedirect("/sorry/")
    return HttpResponseRedirect("/answer-me-here/")
    #return render_to_response("meals/meal/invite/invite_form.html", {'form': form}, context_instance=RequestContext(request))


class InviteCreateView(InviteView, CreateView):
    form_class = InviteForm


class InviteDeleteView(InviteView, DeleteView):

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('meals_invite_list')


class InviteDetailView(InviteView, DetailView):
    pass


class InviteListView(InviteBaseListView, ListView):
    pass


class InviteUpdateView(InviteView, UpdateView):
    pass





