from django.conf.urls.static import static
from django.conf.urls.defaults import patterns, url, include
from django.conf import settings  # Added by Fiber
from django.contrib import admin
from djrill import DjrillAdminSite
from django.views.generic import TemplateView

# Mandrill Email Support
admin.site = DjrillAdminSite()
admin.autodiscover()

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
    url(r'^/?$', TemplateView.as_view(template_name='index.html'), name='home'),
    url(r'^notifications/', include('notification.urls')),
    url(r'^friends/', include('friends.urls')),
    url(r'^friends/suggestions/', include('friends.contrib.suggestions.urls')),
    #==========================================================
    # End Home Page
    #==========================================================
    (r'^', include('meals.urls')),
    (r'^interest/', include('launchpad.urls')),
    #==========================================================
    # Userena
    #==========================================================
    (r'^accounts/', include('userena.urls')),
    (r'^lazysignup/', include('lazysignup.urls')),
    #==========================================================
    # End Userena
    #==========================================================

    #==========================================================
    # Facebook
    #==========================================================
    (r'^facebook/', include('django_facebook.urls')),
    #==========================================================
    # End Facebook
    #==========================================================

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
