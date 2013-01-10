from django.shortcuts import render_to_response
from django.forms import ModelForm
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.views.generic import ListView, DetailView, CreateView, \
                                 DeleteView, UpdateView, \
                                 ArchiveIndexView, DateDetailView, \
                                 DayArchiveView, MonthArchiveView, \
                                 TodayArchiveView, WeekArchiveView, \
                                 YearArchiveView
#from django.views.generic.edit import FormView
#from django.views.generic.detail import SingleObjectTemplateResponseMixin
#from util.widgets import BootstrapSplitDateTimeWidget
from meals.models import Meal
from django.shortcuts import get_object_or_404
from django.template import RequestContext
from django.template.loader import render_to_string
from django.views.decorators.http import require_POST

from meals.models import Meal

from django import forms
import autocomplete_light


class MealForm(ModelForm):
    """
    Provides form for creation and modification, need to explicitly set this.
    """
    #venue = forms.CharField(widget=autocomplete_light.TextWidget('VenueAutocomplete'))

    class Meta:
        model = Meal
        exclude = ('host', 'guests', 'wants', 'needs', 'haves', 'icon', 'description', 'venue', 'current_guests', 'suitable_for', 'parts', 'recipe', 'name')
        # widgets = {
        #     'when': BootstrapSplitDateTimeWidget(attrs={'date_class': 'datepicker-default', 'time_class': 'timepicker-default input-timepicker'}),
        #     #'description': Textarea(attrs={'cols': 40, 'rows': 20})
        # }


def home_view(request):
    # if request.method == "POST":
    #     form = InviteForm(request.POST, request.FILES)
    #     if form.is_valid():
    #         meal = Meal.objects.get(pk=meal_id)
    #         for item in form.cleaned_data:
    #             print item
    #             print "-"
    #         email = form.cleaned_data['email']
    #         # we have a valid email address, we should check if we have a user with that email and add that too maybe.
    #         try:
    #             user = User.objects.get(email=email)[0]
    #             print user
    #         except:
    #             print "no user found"
    #             user = None
    #         if 'max_plusones' in form.cleaned_data:
    #             max_plusones = form.cleaned_data['max_plusones']
    #         else:
    #             max_plusones = 1
    #         invitee = Invitee.objects.get_or_create(email=email)[0]
    #         invitee.user = user
    #         invite = Invite.objects.get_or_create(max_plusones=max_plusones, meal=meal, invitee=invitee)[0]
    #         print invite
    #         #data = _invite_data(request, invite)
    #         #return HttpResponseRedirect(invite.meal.get_absolute_url())
    #         return HttpResponseRedirect(meal.get_absolute_url())
    # else:
    #     form = InviteForm()
    meal_form = MealForm()
    bum = "bumbum"
    return render_to_response("dawn.html", {'meal_form': meal_form}, context_instance=RequestContext(request))
