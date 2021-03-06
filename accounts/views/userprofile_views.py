from django.views.generic import ListView, DetailView, CreateView, \
                                 DeleteView, UpdateView, \
                                 ArchiveIndexView, DateDetailView, \
                                 DayArchiveView, MonthArchiveView, \
                                 TodayArchiveView, WeekArchiveView, \
                                 YearArchiveView


from accounts.models import UserProfile
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


class UserProfileView(object):
    model = UserProfile

    def get_template_names(self):
        """Nest templates within userprofile directory."""
        tpl = super(UserProfileView, self).get_template_names()[0]
        app = self.model._meta.app_label
        mdl = 'userprofile'
        self.template_name = tpl.replace(app, '{0}/{1}'.format(app, mdl))
        return [self.template_name]

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(UserProfileView, self).dispatch(*args, **kwargs)


class UserProfileDateView(UserProfileView):
    date_field = 'date_of_birth'
    month_format = '%m'


class UserProfileBaseListView(UserProfileView):
    paginate_by = 10


class UserProfileArchiveIndexView(
    UserProfileDateView, UserProfileBaseListView, ArchiveIndexView):
    pass


class UserProfileCreateView(UserProfileView, CreateView):
    pass


class UserProfileDateDetailView(UserProfileDateView, DateDetailView):
    pass


class UserProfileDayArchiveView(
    UserProfileDateView, UserProfileBaseListView, DayArchiveView):
    pass


class UserProfileDeleteView(UserProfileView, DeleteView):

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('accounts_userprofile_list')

from actstream.models import actor_stream


class UserProfileDetailView(UserProfileView, DetailView):
    slug_field = 'user'

    def get_context_data(self, **kwargs):
        print self.object
        actionstream = actor_stream(self.object.user)
        print actionstream
        context = {
            'actstream': actionstream
        }
        context.update(kwargs)
        return super(UserProfileDetailView, self).get_context_data(**context)


class UserProfileListView(UserProfileBaseListView, ListView):
    pass


class UserProfileMonthArchiveView(
    UserProfileDateView, UserProfileBaseListView, MonthArchiveView):
    pass


class UserProfileTodayArchiveView(
    UserProfileDateView, UserProfileBaseListView, TodayArchiveView):
    pass


class UserProfileUpdateView(UserProfileView, UpdateView):
    pass


class UserProfileWeekArchiveView(
    UserProfileDateView, UserProfileBaseListView, WeekArchiveView):
    pass


class UserProfileYearArchiveView(
    UserProfileDateView, UserProfileBaseListView, YearArchiveView):
    make_object_list = True



