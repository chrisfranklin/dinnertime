from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns
from api import views


urlpatterns = patterns('api.views',
                       url(r'^home/$', views.index, name='index'),
                       url(r'^$', 'api_root'),

                       url(r'^meals/$', views.MealList.as_view(), name='meal-list'),
                       url(r'^meals/(?P<pk>\d+)/$', views.MealDetail.as_view(), name='meal-detail'),

                       url(r'^mealparts/$', views.MealPartList.as_view(), name='mealpart-list'),
                       url(r'^mealparts/(?P<pk>\d+)/$', views.MealPartDetail.as_view(), name='mealpart-detail'),

                       url(r'^parts/$', views.PartList.as_view(), name='part-list'),
                       url(r'^parts/(?P<pk>\d+)/$', views.PartDetail.as_view(), name='part-detail'),

                       url(r'^guests/$', views.GuestList.as_view(), name='guest-list'),
                       url(r'^guests/(?P<pk>\d+)/$', views.GuestDetail.as_view(), name='guest-detail'),

                       url(r'^invites/$', views.InviteList.as_view(), name='invite-list'),
                       url(r'^invites/(?P<pk>\d+)/$', views.InviteDetail.as_view(), name='invite-detail'),

                       )

urlpatterns = format_suffix_patterns(urlpatterns)
