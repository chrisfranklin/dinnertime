from django.views.generic import ListView, DetailView, CreateView, \
                                 DeleteView, UpdateView


from meals.models import Invite, Invitee, Meal

from accounts.models import UserContact
from django.http import HttpResponseRedirect

from django.contrib.auth.models import User

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


class UserContactAutocomplete(autocomplete_light.AutocompleteGenericBase):
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

    email = forms.CharField(widget=autocomplete_light.ChoiceWidget('InviteAutocomplete'))
    #email = forms.ModelChoiceField(UserContact.objects.all(), widget=autocomplete_light.TextWidget('InviteAutocomplete'))

    # Note that defining *_js_attributes on Autocomplete classes or instances
    # also work.

    class Meta:
        model = Invite
        exclude = ('secret', 'plusones', 'status', 'single_use', 'meal', 'invited_by', 'user', 'invitee', 'max_plusones')


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
        print form.data
        no_contact = False
        if 'email' not in form.data:
            saved_email = form.data['email-autocomplete']
            no_contact = True
            print "no email setting %s" % saved_email
        if form.is_valid() or no_contact:
            meal = Meal.objects.get(pk=meal_id)
            max_plusones = 1
            if no_contact:
                email = saved_email
            else:
                email = form.cleaned_data['email']
                if 'max_plusones' in form.cleaned_data:
                    max_plusones = form.cleaned_data['max_plusones']

            # invitee will attach user for us, yay!
            invitee = Invitee.objects.get_or_create(email=email)[0]
            # except:
            #     print "no user found"
            #     user = None
            invite = Invite.objects.get_or_create(max_plusones=max_plusones, meal=meal, invitee=invitee)[0]
            print invite
            #data = _invite_data(request, invite)
            #return HttpResponseRedirect(invite.meal.get_absolute_url())
            return HttpResponseRedirect(meal.get_absolute_url())
    else:
        form = InviteForm()
    return render_to_response("meals/meal/invite/invite_form.html", {'form': form}, context_instance=RequestContext(request))


def ack_invite(request, meal_id, secret, action=None):
    #meal = Meal.objects.get(pk=meal_id)
    invite = Invite.objects.get(secret=secret, meal=meal_id)  # Add error checking to shrug off invalid invites
    if invite.secret == secret:
        # The secret mathes continue
        if action == "y":
            print "gotcha"
            print request.user
            invite.accept_invite(secret, request.user)
            # Add message to display success
            return HttpResponseRedirect(invite.meal.get_absolute_url())
        elif action == "n":
            invite.decline_invite(None, None)
            return HttpResponseRedirect("/sorry/")
        else:
            return HttpResponseRedirect(invite.get_absolute_url())
    else:
        return HttpResponseRedirect("/invalid-secret/")
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





