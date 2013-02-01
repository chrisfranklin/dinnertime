import json

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

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


def set_max_guests(request, meal_id, direction):
    if meal_id:
        meal_object = get_object_or_404(Meal, pk=meal_id)
        if request.user == meal_object.host or request.user.is_staff:
            if int(direction) == 1:
                meal_object.increase_max_guests()
                return HttpResponseRedirect("/meal/" + meal_id + "/")
            elif int(direction) == 0:
                meal_object.decrease_max_guests()
                return HttpResponseRedirect("/meal/" + meal_id + "/")
            else:
                return HttpResponse('<h1>Please enter a direction, 1 is up, 0 is down.</h1>')
        else:
            return HttpResponse("You are not the host of this meal")
        return HttpResponseNotFound('<h1>Meal not found</h1>')
    else:
        return HttpResponse('<h1>Please enter a meal</h1>')


def _meal_data(request, meal):
    data = {
        "html": render_to_string(
            "_meal.html",
            RequestContext(request, {
                "meal": meal
            })
        )
    }
    return data


@require_POST
def set_max_guests_new(request, pk, direction):
    if pk:
        meal_object = get_object_or_404(Meal, pk=pk)
        if request.user == meal_object.host or request.user.is_staff():
            if int(direction) == 1:
                meal_object.increase_max_guests()
                #return HttpResponseRedirect("/meal/" + meal_id + "/")
            elif int(direction) == 0:
                meal_object.decrease_max_guests()
                #return HttpResponseRedirect("/meal/" + meal_id + "/")
            else:
                return HttpResponse('<h1>Please enter a direction, 1 is up, 0 is down.</h1>')
        else:
            return HttpResponse("You are not the host of this meal")
        return HttpResponseNotFound('<h1>Meal not found</h1>')
    else:
        return HttpResponse('<h1>Please enter a meal</h1>')
    data = _meal_data(request, meal_object)
    return HttpResponse(json.dumps(data), mimetype="application/json")


class AjaxableResponseMixin(object):
    """
    Mixin to add AJAX support to a form.
    Must be used with an object-based FormView (e.g. CreateView)
    """
    def render_to_json_response(self, context, **response_kwargs):
        data = json.dumps(context)
        response_kwargs['content_type'] = 'application/json'
        return HttpResponse(data, **response_kwargs)

    def form_invalid(self, form):
        if self.request.is_ajax():
            return self.render_to_json_response(form.errors, status=400)
        else:
            return super(AjaxableResponseMixin, self).form_invalid(form)

    def form_valid(self, form):
        if self.request.is_ajax():
            data = {
                'pk': form.instance.pk,
            }
            return self.render_to_json_response(data)
        else:
            return super(AjaxableResponseMixin, self).form_valid(form)


class MealView(object):
    """
    Attaches object to class, used as base for other CBVs
    """
    model = Meal

    def get_template_names(self):
        """Nest templates within meal directory."""
        tpl = super(MealView, self).get_template_names()[0]
        app = self.model._meta.app_label
        mdl = 'meal'
        self.template_name = tpl.replace(app, '{0}/{1}'.format(app, mdl))
        return [self.template_name]

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(MealView, self).dispatch(*args, **kwargs)


class MealDateView(MealView):
    """
    Sets up base date view format, used as base for data based CBV's
    """
    date_field = 'when'
    month_format = '%m'


class MealBaseListView(MealView):
    """
    Provides pagination
    """
    paginate_by = 10


class MealArchiveIndexView(
        MealDateView, MealBaseListView, ArchiveIndexView):
    pass

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


class MealCreateView(MealView, AjaxableResponseMixin, CreateView):
    """
    Provides create support
    """
    form_class = MealForm
    #success_url = 'success'
    from django.utils.decorators import method_decorator
    from django.contrib.auth.decorators import login_required
    #from lazysignup.decorators import allow_lazy_user

    def form_valid(self, form):
        # Set the host to request.user on form success
        obj = form.save(commit=False)
        obj.host = self.request.user
        obj.save()
        from django.http import HttpResponseRedirect
        return HttpResponseRedirect('/meal/%s/' % obj.id)

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(MealCreateView, self).dispatch(*args, **kwargs)

    def get_form_kwargs(self, **kwargs):
        # Set host to correct value for form, do not trust the data though.
        kwargs = super(MealCreateView, self).get_form_kwargs(**kwargs)
        kwargs['initial']['host'] = self.request.user
        return kwargs


class MealDateDetailView(MealDateView, DateDetailView):
    pass


class MealDayArchiveView(
        MealDateView, MealBaseListView, DayArchiveView):
    pass


class MealDeleteView(MealView, DeleteView):
    """
    Provides delete support
    """

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('meals_meal_list')

from django.views.generic.edit import FormMixin

from actstream.models import action_object_stream
import autocomplete_light
from django import forms
from meals.models import Part


class PartAutocomplete(autocomplete_light.AutocompleteModelBase):
    search_fields = ('name',)

    # Note that defining *_js_attributes in a Widget also works. Widget has
    # priority since it's the most specific.
    autocomplete_js_attributes = {
        'placeholder': 'name of the item',
    }

autocomplete_light.register(Part, PartAutocomplete)


class PartForm(forms.Form):
    name = forms.CharField()

    class Meta:
        pass
        widgets = {
            'name': autocomplete_light.TextWidget('PartAutocomplete'),
        }
        #name = autocomplete_light.get_widgets_dict(Part)


def add_part(request, meal_id, status):  # change this to part

    if request.method == 'POST':  # If the form has been submitted...
        form = PartForm(request.POST)  # A form bound to the POST data
        if form.is_valid():  # All validation rules pass
            # Process the data in form.cleaned_data
            # ...
            name = form.cleaned_data['name']
            meal_object = Meal.objects.get(pk=meal_id)
            if status == "HAVE":
                meal_object.add_have(name, request.user)
            elif status == "NEED":
                meal_object.add_need(name, request.user)
            elif status == "WANT":
                meal_object.add_want(name, request.user)
            else:
                return HttpResponse("Please select have need or want or write generic view.")
            return HttpResponseRedirect(meal_object.get_absolute_url())  # Redirect after POST
    return HttpResponse("No post data or an error has occured")



from meals.models import Venue
# from accounts.models import UserContact


class VenueForm(forms.Form):
    address = forms.CharField(widget=autocomplete_light.ChoiceWidget('VenueAutocomplete'))

def add_venue(request, meal_id):  # change this to part

    if request.method == 'POST':  # If the form has been submitted...
        form = VenueForm(request.POST)  # A form bound to the POST data
        print form.data
        no_venue = False
        if 'address' not in form.data:
            saved_venue = form.data['address-autocomplete']
            no_venue = True
            print "no venue setting %s" % saved_venue
        if form.is_valid() or no_venue:  # All validation rules pass
            # Process the data in form.cleaned_data
            # ...
            if no_venue:
                address = saved_venue
            else:
                address = form.cleaned_data['address']
            meal_object = Meal.objects.get(pk=meal_id)
            meal_object.venue, created = Venue.objects.get_or_create(address=address, user=request.user)
            meal_object.save()
            #meal_object.add_venue(address, request.user)

            return HttpResponseRedirect(meal_object.get_absolute_url())  # Redirect after POST
    return HttpResponse("No post data or an error has occured")

class RecipeForm(forms.Form):
    recipe = forms.CharField(widget=autocomplete_light.ChoiceWidget('RecipeRestAutocomplete'))

class MealDetailView(MealView, DetailView, FormMixin):
    from meals.views.invite_views import InviteForm
    form_class = InviteForm

    def get_context_data(self, **kwargs):
        print self.object
        actionstream = action_object_stream(self.object)
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        formpart = PartForm()
        formvenue = VenueForm()
        formrecipe = RecipeForm()
        print actionstream
        context = {
            'form': form,
            'formh': formpart,
            'formn': formpart,
            'formw': formpart,
            'formv': formvenue,
            'actstream': actionstream,
            'formr': formrecipe
        }
        context.update(kwargs)
        return super(MealDetailView, self).get_context_data(**context)


class MealListView(MealBaseListView, ListView):
    pass

    def get_context_data(self, **kwargs):
        all_meals = Meal.objects.all()
        public_meals = all_meals.filter(privacy="PUBLIC")
        print "PUBLIC MEALS: %s" % public_meals
        attending_meals = all_meals.filter(guests=self.request.user)
        hosted_meals = all_meals.filter(host=self.request.user)
        print "ATTENDING MEALS: %s" % attending_meals
        from meals.models import Invite
        invites = Invite.objects.filter(invitee__user=self.request.user)
        print self.request.user
        context = {
            'public_meals': public_meals,
            'attending_meals': attending_meals,
            'hosting_meals': hosted_meals,
            'invites': invites,
        }
        context.update(kwargs)
        return super(MealListView, self).get_context_data(**context)


class MealMonthArchiveView(
        MealDateView, MealBaseListView, MonthArchiveView):
    pass


class MealTodayArchiveView(
        MealDateView, MealBaseListView, TodayArchiveView):
    pass


class MealUpdateView(MealView, UpdateView):
    """
    Provides update support
    """
    form_class = MealForm


class MealWeekArchiveView(
        MealDateView, MealBaseListView, WeekArchiveView):
    pass


class MealYearArchiveView(
        MealDateView, MealBaseListView, YearArchiveView):
    make_object_list = True
