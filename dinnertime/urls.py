from django.conf.urls.static import static
from django.conf.urls.defaults import patterns, url, include
from django.conf import settings  # Added by Fiber
from django.contrib import admin
from djrill import DjrillAdminSite
from django.views.generic import TemplateView
import autocomplete_light
from dinnertime.views import home_view
autocomplete_light.autodiscover()
# Mandrill Email Support
admin.site = DjrillAdminSite()
admin.autodiscover()

js_info_dict = {
    'packages': ('django.conf',),
}

urlpatterns = patterns('',
   # (r'', include('dinnertime.apps.')),
    #==========================================================
    # Admin Section
    #==========================================================
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^admin/', include(admin.site.urls)),
    #==========================================================
    # End Admin Section
    #==========================================================

    #==========================================================
    # Home Page - Not managed by cms but provided by index.html
    #==========================================================
    #url(r'^/?$', TemplateView.as_view(template_name='index.html'), name='home'),

    url(r'^/?$', home_view, name='home_view'),
    url(r'^notifications/', include('notification.urls')),
    url(r'^friends/', include('friends.urls')),
    url(r'^friends/suggestions/', include('friends.contrib.suggestions.urls')),
    #==========================================================
    # End Home Page
    #==========================================================
    (r'^', include('meals.urls')),
    (r'^interest/', include('launchpad.urls')),
    #==========================================================
    # Allauth
    #==========================================================
    (r'^accounts/', include('allauth.urls')),
    (r'^accounts/', include('accounts.urls')),
    #==========================================================
    # End Userena
    #==========================================================

    #==========================================================
    # Facebook
    #==========================================================
    #(r'^facebook/', include('django_facebook.urls')),
    #==========================================================
    # End Facebook
    #==========================================================
    url(r'autocomplete/', include('autocomplete_light.urls')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    (r'^comments/', include('django.contrib.comments.urls')),
    (r'^inplaceeditform/', include('inplaceeditform.urls')),
    (r'^jsi18n$', 'django.views.i18n.javascript_catalog', js_info_dict),
    (r'^activity/', include('actstream.urls')),
    url(r"^likes/", include("phileo.urls")),
    (r'^avatar/', include('avatar.urls')),
    #(r'^feedback/', include('django_basic_feedback.urls')),
)

if 'api' in settings.INSTALLED_APPS:
    urlpatterns += patterns('',
            (r'^api/', include('api.urls')),
        )

from django.conf.urls import patterns, url, include
from rest_framework.urlpatterns import format_suffix_patterns



# urlpatterns += patterns('meals.api',
#     url(r'^api/$', 'api_root'),
#     url(r'^api/meals/$', MealList.as_view(), name='meal-list'),
#     url(r'^api/meals/(?P<pk>\d+)/$', MealDetail.as_view(), name='meal-detail'),
# )

# Format suffixes
#urlpatterns = format_suffix_patterns(urlpatterns, allowed=['json', 'api'])

from django_statsd.urls import urlpatterns as statsd_patterns

urlpatterns += patterns('',
        ('^services/timing/', include(statsd_patterns)),
)


OAUTH_ACCESS_SETTINGS = {
    'twitter': {
        'keys': {
            'KEY': 'YOURAPPKEY',
            'SECRET': 'yourappsecretcode',
        },
        'endpoints': {
            'request_token': 'https://api.twitter.com/oauth/request_token',
            'authorize': 'http://twitter.com/oauth/authorize',
            'access_token': 'https://twitter.com/oauth/request_token',
            'callback': 'friends.contrib.suggestions.views.import_twitter_contacts',
        },
    },
    'yahoo': {
        'keys': {
            'KEY': 'dj0yJmk9TFRkU0pzQmZxV3VQJmQ9WVdrOWQwSTFNVEl6TkRJbWNHbzlPRFkzTnpjNE9UWXkmcz1jb25zdW1lcnNlY3JldCZ4PTVh',
            'SECRET': '65f01ba9732452c323af561ebee4094b42a9674f',
        },
        'endpoints': {
            'request_token': 'https://api.login.yahoo.com/oauth/v2/get_request_token',
            'authorize': 'https://api.login.yahoo.com/oauth/v2/request_auth',
            'access_token': 'https://api.login.yahoo.com/oauth/v2/get_token',
            'callback': 'friends.contrib.suggestions.views.import_yahoo_contacts',
        },
    },
}

if settings.DEBUG and settings.MEDIA_ROOT:
    urlpatterns += static(settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT)
