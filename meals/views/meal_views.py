import json

from django.forms import ModelForm
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView, \
                                 DeleteView, UpdateView, \
                                 ArchiveIndexView, DateDetailView, \
                                 DayArchiveView, MonthArchiveView, \
                                 TodayArchiveView, WeekArchiveView, \
                                 YearArchiveView
#from django.views.generic.edit import FormView
#from django.views.generic.detail import SingleObjectTemplateResponseMixin
from util.widgets import BootstrapSplitDateTimeWidget
from meals.models import Meal


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
    model = Meal

    def get_template_names(self):
        """Nest templates within meal directory."""
        tpl = super(MealView, self).get_template_names()[0]
        app = self.model._meta.app_label
        mdl = 'meal'
        self.template_name = tpl.replace(app, '{0}/{1}'.format(app, mdl))
        return [self.template_name]


class MealDateView(MealView):
    date_field = 'when'
    month_format = '%m'


class MealBaseListView(MealView):
    paginate_by = 10


class MealArchiveIndexView(
    MealDateView, MealBaseListView, ArchiveIndexView):
    pass


class MealForm(ModelForm):

    class Meta:
        model = Meal
        exclude = ('host', 'guests', 'wants', 'needs', 'haves', 'icon', 'description', 'venue')
        widgets = {
            'when': BootstrapSplitDateTimeWidget(attrs={'date_class': 'datepicker-default', 'time_class': 'timepicker-default input-timepicker'}),
            #'description': Textarea(attrs={'cols': 40, 'rows': 20})
        }


class MealCreateView(MealView, AjaxableResponseMixin, CreateView):
    form_class = MealForm
    #success_url = 'success'

    def get_form_kwargs(self, **kwargs):
        # pass "user" keyword argument with the current user to your form
        kwargs = super(MealCreateView, self).get_form_kwargs(**kwargs)
        kwargs['initial']['host'] = self.request.user
        return kwargs


class MealDateDetailView(MealDateView, DateDetailView):
    pass


class MealDayArchiveView(
    MealDateView, MealBaseListView, DayArchiveView):
    pass


class MealDeleteView(MealView, DeleteView):

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('meals_meal_list')


class MealDetailView(MealView, DetailView):
    pass


class MealListView(MealBaseListView, ListView):
    pass


class MealMonthArchiveView(
    MealDateView, MealBaseListView, MonthArchiveView):
    pass


class MealTodayArchiveView(
    MealDateView, MealBaseListView, TodayArchiveView):
    pass


class MealUpdateView(MealView, UpdateView):
    form_class = MealForm


class MealWeekArchiveView(
    MealDateView, MealBaseListView, WeekArchiveView):
    pass


class MealYearArchiveView(
    MealDateView, MealBaseListView, YearArchiveView):
    make_object_list = True
