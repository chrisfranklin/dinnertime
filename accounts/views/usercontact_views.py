from django.views.generic import ListView, DetailView, CreateView, \
                                 DeleteView, UpdateView


from accounts.models import UserContact


class UserContactView(object):
    model = UserContact

    def get_template_names(self):
        """Nest templates within usercontact directory."""
        tpl = super(UserContactView, self).get_template_names()[0]
        app = self.model._meta.app_label
        mdl = 'usercontact'
        self.template_name = tpl.replace(app, '{0}/{1}'.format(app, mdl))
        return [self.template_name]


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


class UserContactListView(UserContactBaseListView, ListView):
    pass




class UserContactUpdateView(UserContactView, UpdateView):
    pass





