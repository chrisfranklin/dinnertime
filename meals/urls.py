from django.conf.urls import patterns, url

from meals.views.venue_views import *
urlpatterns = patterns('',

    url(
        regex=r'^venue/create/$',
        view=VenueCreateView.as_view(),
        name='meals_venue_create'
    ),


    url(
        regex=r'^venue/(?P<pk>\d+?)/delete/$',
        view=VenueDeleteView.as_view(),
        name='meals_venue_delete'
    ),
    url(
        regex=r'^venue/(?P<pk>\d+?)/$',
        view=VenueDetailView.as_view(),
        name='meals_venue_detail'
    ),
    url(
        regex=r'^venue/$',
        view=VenueListView.as_view(),
        name='meals_venue_list'
    ),


    url(
        regex=r'^venue/(?P<pk>\d+?)/update/$',
        view=VenueUpdateView.as_view(),
        name='meals_venue_update'
    ),


)



from meals.views.invite_views import *
urlpatterns += patterns('',

    url(
        regex=r'^invite/create/$',
        view=InviteCreateView.as_view(),
        name='meals_invite_create'
    ),


    url(
        regex=r'^invite/(?P<pk>\d+?)/delete/$',
        view=InviteDeleteView.as_view(),
        name='meals_invite_delete'
    ),
    url(
        regex=r'^invite/(?P<pk>\d+?)/$',
        view=InviteDetailView.as_view(),
        name='meals_invite_detail'
    ),
    url(
        regex=r'^invite/$',
        view=InviteListView.as_view(),
        name='meals_invite_list'
    ),


    url(
        regex=r'^invite/(?P<pk>\d+?)/update/$',
        view=InviteUpdateView.as_view(),
        name='meals_invite_update'
    ),


)

from meals.views.meal_views import *
urlpatterns += patterns('',
    # ex: /polls/5/vote/
    url(r'^meal/(?P<meal_id>\d+)/max_guests/(?P<direction>\d+)$', set_max_guests, name='increase_max_guest'),
    url(r'^meal/(?P<meal_id>\d+)/max_guests/(?P<direction>\d+)/$', set_max_guests, name='decrease_max_guest'),
    url(r'^meal/(?P<meal_id>\d+)/part/add/(?P<status>\w+)/$', add_part, name='meals_meal_part_create'),
)
urlpatterns += patterns('',
    url(
        regex=r'^meal/archive/$',
        view=MealArchiveIndexView.as_view(),
        name='meals_meal_archive_index'
    ),
    url(
        regex=r'^meal/(?P<meal_id>\d+?)/invite/create/$',
        view=add_invite,
        name='meals_meal_invite_create'
    ),
    url(
        regex=r'^meal/(?P<meal_id>\d+?)/invite/update/$',
        view=add_invite,
        name='meals_meal_invite_update'
    ),
    url(
        regex=r'^meal/(?P<meal_id>\d+?)/invite/(?P<secret>\w+?)/$',
        view=ack_invite,
        name='meals_meal_invite_ack'
    ),
    url(
        regex=r'^meal/(?P<meal_id>\d+?)/invite/(?P<secret>\w+?)/(?P<action>\w+?)/$',
        view=ack_invite,
        name='meals_meal_invite_ack'
    ),
    
    url(
        regex=r'^meal/create/$',
        view=MealCreateView.as_view(),
        name='meals_meal_create'
    ),
    url(
        regex=r'^meal/(?P<year>\d{4})/'
               r'(?P<month>\d{1,2})/'
               r'(?P<day>\d{1,2})/'
               r'(?P<pk>\d+?)/$',
        view=MealDateDetailView.as_view(),
        name='meals_meal_date_detail'
    ),
    url(
        regex=r'^meal/archive/(?P<year>\d{4})/'
               r'(?P<month>\d{1,2})/'
               r'(?P<day>\d{1,2})/$',
        view=MealDayArchiveView.as_view(),
        name='meals_meal_day_archive'
    ),
    url(
        regex=r'^meal/(?P<pk>\d+?)/delete/$',
        view=MealDeleteView.as_view(),
        name='meals_meal_delete'
    ),
    url(
        regex=r'^meal/(?P<pk>\d+?)/$',
        view=MealDetailView.as_view(),
        name='meals_meal_detail'
    ),
    url(
        regex=r'^meal/$',
        view=MealListView.as_view(),
        name='meals_meal_list'
    ),
    url(
        regex=r'^meal/archive/(?P<year>\d{4})/'
               r'(?P<month>\d{1,2})/$',
        view=MealMonthArchiveView.as_view(),
        name='meals_meal_month_archive'
    ),
    url(
        regex=r'^meal/today/$',
        view=MealTodayArchiveView.as_view(),
        name='meals_meal_today_archive'
    ),
    url(
        regex=r'^meal/(?P<pk>\d+?)/update/$',
        view=MealUpdateView.as_view(),
        name='meals_meal_update'
    ),
    url(
        regex=r'^meal/archive/(?P<year>\d{4})/'
               '(?P<month>\d{1,2})/'
               'week/(?P<week>\d{1,2})/$',
        view=MealWeekArchiveView.as_view(),
        name='meals_meal_week_archive'
    ),
    url(
        regex=r'^meal/archive/(?P<year>\d{4})/$',
        view=MealYearArchiveView.as_view(),
        name='meals_meal_year_archive'
    ),
)
