from django.views.generic import ListView, DetailView, CreateView, \
                                 DeleteView, UpdateView


from meals.models import Invite


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



class InviteCreateView(InviteView, CreateView):
    pass




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





