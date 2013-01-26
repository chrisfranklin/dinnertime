from django.conf.urls import patterns, url


from accounts.views.userprofile_views import *
urlpatterns = patterns('',
                       # url(
                       # regex=r'^userprofile/archive/$',
                       # view=UserProfileArchiveIndexView.as_view(),
                       # name='accounts_userprofile_archive_index'
                       # ),
                       # url(
                       # regex=r'^userprofile/create/$',
                       # view=UserProfileCreateView.as_view(),
                       # name='accounts_userprofile_create'
                       # ),
                       # url(
                       # regex=r'^userprofile/(?P<year>\d{4})/'
                       # '(?P<month>\d{1,2})/'
                       # '(?P<day>\d{1,2})/'
                       # '(?P<pk>\d+?)/$',
                       # view=UserProfileDateDetailView.as_view(),
                       # name='accounts_userprofile_date_detail'
                       # ),
                       # url(
                       # regex=r'^userprofile/archive/(?P<year>\d{4})/'
                       # '(?P<month>\d{1,2})/'
                       # '(?P<day>\d{1,2})/$',
                       # view=UserProfileDayArchiveView.as_view(),
                       # name='accounts_userprofile_day_archive'
                       # ),
                       # url(
                       # regex=r'^userprofile/(?P<pk>\d+?)/delete/$',
                       # view=UserProfileDeleteView.as_view(),
                       # name='accounts_userprofile_delete'
                       # ),
                       url(
                       regex=r'^userprofile/(?P<pk>\d+)/$',
                       view=UserProfileDetailView.as_view(),
                       name='accounts_userprofile_detail'
                       ),
                       # dupe hack below
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
                       # url(
                       # regex=r'^userprofile/archive/(?P<year>\d{4})/'
                       # '(?P<month>\d{1,2})/$',
                       # view=UserProfileMonthArchiveView.as_view(),
                       # name='accounts_userprofile_month_archive'
                       # ),
                       # url(
                       # regex=r'^userprofile/today/$',
                       # view=UserProfileTodayArchiveView.as_view(),
                       # name='accounts_userprofile_today_archive'
                       # ),
                       url(
                       regex=r'^userprofile/(?P<pk>\d+?)/update/$',
                       view=UserProfileUpdateView.as_view(),
                       name='accounts_userprofile_update'
                       ),
                       # url(
                       # regex=r'^userprofile/archive/(?P<year>\d{4})/'
                       # '(?P<month>\d{1,2})/'
                       # 'week/(?P<week>\d{1,2})/$',
                       # view=UserProfileWeekArchiveView.as_view(),
                       # name='accounts_userprofile_week_archive'
                       # ),
                       # url(
                       # regex=r'^userprofile/archive/(?P<year>\d{4})/$',
                       # view=UserProfileYearArchiveView.as_view(),
                       # name='accounts_userprofile_year_archive'
                       # ),
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
