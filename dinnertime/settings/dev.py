"""Settings for Development Server"""
from dinnertime.settings.base import *   # pylint: disable=W0614,W0401

DEBUG = True
TEMPLATE_DEBUG = DEBUG

VAR_ROOT = '/var/www/dinnertime'
MEDIA_ROOT = os.path.join(VAR_ROOT, 'uploads')
STATIC_ROOT = os.path.join(VAR_ROOT, 'static')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'dinnertime',
#        'USER': 'dbuser',
#        'PASSWORD': 'dbpassword',
    }
}

print DATABASES

INSTALLED_APPS += (
    # 'dinnertime.apps.',
    'debug_toolbar',
    
)


#==============================================================================
# Middleware
#==============================================================================

MIDDLEWARE_CLASSES += (

    #--------------------------------------------------------------------------
    # Django Debug Toolbar
    #            after middleware encoding response's content eg GZipMiddleware
    #            before any you want the debug toolbar on.
    #--------------------------------------------------------------------------
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    #--------------------------------------------------------------------------
    # End Django Debug Toolbar
    #--------------------------------------------------------------------------
)

# WSGI_APPLICATION = 'dinnertime.wsgi.dev.application'

#==============================================================================
# Facebook Settings - Development
#==============================================================================
FACEBOOK_APP_ID = "114345905396999"
FACEBOOK_APP_SECRET = "31de98e45c859806cf8fc286129d91fe"