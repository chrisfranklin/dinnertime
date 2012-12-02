"""Base settings shared by all environments"""
# Import global settings to make it easier to extend settings.
from django.conf.global_settings import *   # pylint: disable=W0614,W0401

#==============================================================================
# Background Tasks
#==============================================================================
import djcelery
djcelery.setup_loader()

#==============================================================================
# Generic Django project settings
#==============================================================================

DEBUG = True
TEMPLATE_DEBUG = DEBUG

SITE_ID = 1
# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
TIME_ZONE = 'UTC'
USE_TZ = True
USE_I18N = True
USE_L10N = True
LANGUAGE_CODE = 'en'
LANGUAGES = (
    ('en', 'English'),
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = 's^tsuf-^w*w&amp;&amp;)#-_9xh2l8r$qs4itiq8h1a2aft&amp;rjj^7#9aj'

INSTALLED_APPS = (
    # 'dinnertime.apps.',

    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'django.contrib.admindocs',

    #'south',

    #==========================================================================
    # 3rd party Applications
    #==========================================================================

    #--------------------------------------------------------------------------
    # User Profiles
    #--------------------------------------------------------------------------
    'accounts',

    #--------------------------------------------------------------------------
    # Theme
    #--------------------------------------------------------------------------
    #'bootstrap',

    #--------------------------------------------------------------------------
    # Email
    #--------------------------------------------------------------------------
    'djrill',

    #--------------------------------------------------------------------------
    # Fiber and Fiber prerequisites
    #--------------------------------------------------------------------------
    'djangorestframework',
    'mptt',
    'compressor',
    'fiber',

    #--------------------------------------------------------------------------
    # Reversion history for models
    #--------------------------------------------------------------------------
    'reversion',

    #--------------------------------------------------------------------------
    # Userena Accounts Management
    #--------------------------------------------------------------------------
    'userena',
    'guardian',

    #--------------------------------------------------------------------------
    # Facebook Support
    #--------------------------------------------------------------------------

    #--------------------------------------------------------------------------
    # Background Task Support
    #--------------------------------------------------------------------------
    'djcelery',

    
)

#==============================================================================
# Calculation of directories relative to the project module location
#==============================================================================

import os
import sys
import dinnertime as project_module

PROJECT_DIR = os.path.dirname(os.path.realpath(project_module.__file__))

PYTHON_BIN = os.path.dirname(sys.executable)
ve_path = os.path.dirname(os.path.dirname(os.path.dirname(PROJECT_DIR)))
# Assume that the presence of 'activate_this.py' in the python bin/
# directory means that we're running in a virtual environment.
if os.path.exists(os.path.join(PYTHON_BIN, 'activate_this.py')):
    # We're running with a virtualenv python executable.
    VAR_ROOT = os.path.join(os.path.dirname(PYTHON_BIN), 'var')
elif ve_path and os.path.exists(os.path.join(ve_path, 'bin',
        'activate_this.py')):
    # We're running in [virtualenv_root]/src/[project_name].
    VAR_ROOT = os.path.join(ve_path, 'var')
else:
    # Set the variable root to a path in the project which is
    # ignored by the repository.
    VAR_ROOT = os.path.join(PROJECT_DIR, 'var')

if not os.path.exists(VAR_ROOT):
    os.mkdir(VAR_ROOT)

#==============================================================================
# Project URLS and media settings
#==============================================================================

ROOT_URLCONF = 'dinnertime.urls'

LOGIN_REDIRECT_URL = '/'
LOGIN_URL = '/accounts/signin/'
LOGOUT_URL = '/accounts/signout/'
ANONYMOUS_USER_ID = -1

AUTH_PROFILE_MODULE = 'accounts.UserProfile' # THIS SHOULD BE SET TO PROFILE MODEL



STATIC_URL = '/static/'
MEDIA_URL = '/uploads/'

STATIC_ROOT = os.path.join(VAR_ROOT, 'static')
MEDIA_ROOT = os.path.join(VAR_ROOT, 'uploads')

STATICFILES_DIRS = (
    os.path.join(PROJECT_DIR, 'static'),
)

#==============================================================================
# Static Files Finders
#==============================================================================

STATICFILES_FINDERS += (
    'compressor.finders.CompressorFinder',
)

#==============================================================================
# Templates
#==============================================================================

TEMPLATE_DIRS = (
    os.path.join(PROJECT_DIR, 'templates'),
)

TEMPLATE_CONTEXT_PROCESSORS += (
    'django.core.context_processors.request',
)

#==============================================================================
# Middleware
#==============================================================================

MIDDLEWARE_CLASSES += (
    #--------------------------------------------------------------------------
    # Fiber Content Management System
    #--------------------------------------------------------------------------
    'fiber.middleware.ObfuscateEmailAddressMiddleware',
    'fiber.middleware.AdminPageMiddleware',
    #--------------------------------------------------------------------------
    # End Fiber
    #--------------------------------------------------------------------------
)

#==============================================================================
# Auth / security
#==============================================================================

AUTHENTICATION_BACKENDS += (
    'userena.backends.UserenaAuthenticationBackend',
    'guardian.backends.ObjectPermissionBackend',
    'django.contrib.auth.backends.ModelBackend',
)

#==============================================================================
# Cache Framework - set to memcache
#==============================================================================

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '127.0.0.1:11211',
    }
}

#==============================================================================
# Logging and Data gathering 
#==============================================================================


#==============================================================================
# Email Settings
#==============================================================================

EMAIL_BACKEND = 'djrill.mail.backends.djrill.DjrillBackend'
MANDRILL_API_KEY = 'set-your-own-key-here'
MANDRILL_API_URL = 'http://mandrillapp.com/api/1.0'

#==============================================================================
# Miscellaneous project settings
#==============================================================================

#==============================================================================
# Third party app settings
#==============================================================================
