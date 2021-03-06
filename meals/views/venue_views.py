from django.views.generic import ListView, DetailView, CreateView, \
    DeleteView, UpdateView


from meals.models import Venue
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


class VenueView(object):
    model = Venue

    def get_template_names(self):
        """Nest templates within venue directory."""
        tpl = super(VenueView, self).get_template_names()[0]
        app = self.model._meta.app_label
        mdl = 'venue'
        self.template_name = tpl.replace(app, '{0}/{1}'.format(app, mdl))
        return [self.template_name]

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(VenueView, self).dispatch(*args, **kwargs)


class VenueBaseListView(VenueView):
    paginate_by = 10


class VenueCreateView(VenueView, CreateView):
    pass


class VenueDeleteView(VenueView, DeleteView):

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('meals_venue_list')


class VenueDetailView(VenueView, DetailView):
    pass


class VenueListView(VenueBaseListView, ListView):
    pass


class VenueUpdateView(VenueView, UpdateView):
    pass
