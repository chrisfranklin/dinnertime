from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns
from api import views


urlpatterns = patterns('api.views',
                       url(r'^home/$', views.index, name='index'),
                       url(r'^$', 'api_root'),
                       url(r'^meals/$', views.MealList.as_view(), name='meal-list'),
                       url(r'^meals/(?P<pk>\d+)/$', views.MealDetail.as_view(), name='meal-detail'),
                       )

urlpatterns = format_suffix_patterns(urlpatterns)
