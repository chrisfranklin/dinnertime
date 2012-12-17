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


def set_max_guests(request, meal_id, direction):
    if meal_id:
        meal_object = get_object_or_404(Meal, pk=meal_id)
        if request.user == meal_object.host or request.user.is_staff():
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


class MealForm(ModelForm):
    """
    Provides form for creation and modification, need to explicitly set this.
    """
    class Meta:
        model = Meal
        exclude = ('host', 'guests', 'wants', 'needs', 'haves', 'icon', 'description', 'venue', 'current_guests', 'suitable_for', 'parts')
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
    from lazysignup.decorators import allow_lazy_user

    def form_valid(self, form):
        # Set the host to request.user on form success
        obj = form.save(commit=False)
        obj.host = self.request.user
        obj.save()
        from django.http import HttpResponseRedirect
        return HttpResponseRedirect('/meal/%s/' % obj.id)

    @method_decorator(allow_lazy_user)
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
from meals.views.invite_views import InviteForm
from actstream.models import action_object_stream
from django import forms


class HaveForm(forms.Form):
    name = forms.CharField(max_length=100)
    status = "HAVE"


class NeedForm(forms.Form):
    name = forms.CharField(max_length=100)
    status = "NEED"


class WantForm(forms.Form):
    name = forms.CharField(max_length=100)
    status = "WANT"

from django.shortcuts import render


def add_part(request, meal_id, status):  # change this to part
    if status == "HAVE":
        if request.method == 'POST':  # If the form has been submitted...
            form = HaveForm(request.POST)  # A form bound to the POST data
            if form.is_valid():  # All validation rules pass
                # Process the data in form.cleaned_data
                # ...
                name = form.cleaned_data['name']
                meal_object = Meal.objects.get(pk=meal_id)
                meal_object.add_have(name, request.user)
                return HttpResponseRedirect(meal_object.get_absolute_url())  # Redirect after POST
        else:
            form = HaveForm()  # An unbound form

        return render(request, 'meals/meal/meal_part_form.html', {
            'form': form,
        })
    else:
        return HttpResponse("Invalid part status i.e. not have")


class MealDetailView(MealView, DetailView, FormMixin):
    form_class = InviteForm

    def get_context_data(self, **kwargs):
        print self.object
        actionstream = action_object_stream(self.object)
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        formh = HaveForm()
        formn = NeedForm()
        formw = WantForm()
        print actionstream
        context = {
            'form': form,
            'formh': formh,
            'formn': formn,
            'formw': formw,
            'actstream': actionstream
        }
        context.update(kwargs)
        return super(MealDetailView, self).get_context_data(**context)


class MealListView(MealBaseListView, ListView):
    pass


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
