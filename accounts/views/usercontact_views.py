from django.views.generic import ListView, DetailView, CreateView, \
                                 DeleteView, UpdateView


from accounts.models import UserContact
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator



class UserContactView(object):
    model = UserContact

    def get_template_names(self):
        """Nest templates within usercontact directory."""
        tpl = super(UserContactView, self).get_template_names()[0]
        app = self.model._meta.app_label
        mdl = 'usercontact'
        self.template_name = tpl.replace(app, '{0}/{1}'.format(app, mdl))
        return [self.template_name]

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(UserContactView, self).dispatch(*args, **kwargs)


class UserContactBaseListView(UserContactView):
    paginate_by = 10



class UserContactCreateView(UserContactView, CreateView):
    pass




class UserContactDeleteView(UserContactView, DeleteView):

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('accounts_usercontact_list')


class UserContactDetailView(UserContactView, DetailView):
    pass


class UserContactListView(UserContactView, ListView):
    pass

    def get_context_data(self, **kwargs):
        contacts = UserContact.objects.filter(owner=self.request.user)
        context = {
            'contact_list': contacts,
        }
        context.update(kwargs)
        return super(UserContactListView, self).get_context_data(**context)


class UserContactUpdateView(UserContactView, UpdateView):
    pass


