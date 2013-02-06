from django.conf.urls import patterns, url


from accounts.views.userprofile_views import *
urlpatterns = patterns('',
                       url(
                       regex=r'^userprofile/(?P<pk>\d+)/$',
                       view=UserProfileDetailView.as_view(),
                       name='accounts_userprofile_detail'
                       ),
                       # dupe hack below  TODO: revisit this and make profiles work with username slug
                       url(
                       regex=r'^userprofile/(?P<pk>\d+)/$',
                       view=UserProfileDetailView.as_view(),
                       name='profile_detail'
                       ),
                       url(
                       regex=r'^userprofile/$',
                       view=UserProfileListView.as_view(),
                       name='accounts_userprofile_list'
                       ),
                       url(
                       regex=r'^userprofile/(?P<pk>\d+?)/update/$',
                       view=UserProfileUpdateView.as_view(),
                       name='accounts_userprofile_update'
                       ),
                       )


from accounts.views.usercontact_views import *
urlpatterns += patterns('',
                        url(
                        regex=r'^usercontact/create/$',
                        view=UserContactCreateView.as_view(),
                        name='accounts_usercontact_create'
                        ),
                        url(
                        regex=r'^usercontact/(?P<pk>\d+?)/delete/$',
                        view=UserContactDeleteView.as_view(),
                        name='accounts_usercontact_delete'
                        ),
                        url(
                        regex=r'^usercontact/(?P<pk>\d+?)/$',
                        view=UserContactDetailView.as_view(),
                        name='accounts_usercontact_detail'
                        ),
                        url(
                        regex=r'^usercontact/$',
                        view=UserContactListView.as_view(),
                        name='accounts_usercontact_list'
                        ),
                        url(
                        regex=r'^usercontact/(?P<pk>\d+?)/update/$',
                        view=UserContactUpdateView.as_view(),
                        name='accounts_usercontact_update'
                        ),
                        )
