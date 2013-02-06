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

    class Meta:
        model = Meal
        exclude = ('host', 'guests', 'wants', 'needs', 'haves', 'icon', 'description', 'venue', 'current_guests', 'suitable_for', 'parts', 'recipe', 'name')


def home_view(request):
    """
    Serves the index page for the site.
    """
    meal_form = MealForm()
    bum = "bumbum"
    return render_to_response("index.html", {'meal_form': meal_form}, context_instance=RequestContext(request))
