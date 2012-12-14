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

ADMINS = (
    ('chris', 'chris@piemonster.me'),
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = 's^tsuf-^w*w&amp;&amp;)#-_9xh2l8r$qs4itiq8h1a2aft&amp;rjj^7#9aj'

INSTALLED_APPS = (
    # 'dinnertime.apps.',

    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.syndication',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'django.contrib.admindocs',
    'django.contrib.comments',

    #'south',
    'meals',
    'util',

    'easy_maps',

    'rest_framework',

    'autocomplete_light',

    'lazysignup',
    #'django_facebook',  DEPRECATED, remove soon
    'django_gravatar',
    'crispy_forms',

    'friends',
    'oauth_access',
    'friends.contrib.suggestions',
    'notification',
    'launchpad',

    #==========================================================================
    # 3rd party Applications
    #==========================================================================
    #'django_jenkins',
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
    # Util
    #--------------------------------------------------------------------------
    'mptt',
    'compressor',

    #--------------------------------------------------------------------------
    # Reversion history for models
    #--------------------------------------------------------------------------
    #'reversion',

    #--------------------------------------------------------------------------
    # Allauth Accounts Management
    #--------------------------------------------------------------------------
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.facebook',
    'allauth.socialaccount.providers.google',
    # 'allauth.socialaccount.providers.github',
    # 'allauth.socialaccount.providers.linkedin',
    # 'allauth.socialaccount.providers.openid',
    # 'allauth.socialaccount.providers.persona',
    # 'allauth.socialaccount.providers.soundcloud',
    # 'allauth.socialaccount.providers.twitter',

    #--------------------------------------------------------------------------
    # Facebook Support
    #--------------------------------------------------------------------------

    #--------------------------------------------------------------------------
    # Background Task Support
    #--------------------------------------------------------------------------
    'djcelery',

    'inplaceeditform',
    'actstream',
    'phileo',

)


PHILEO_LIKABLE_MODELS = {

    "meals.Meal": {}  # can override default config settings for each model here

}


print (INSTALLED_APPS)

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

AUTH_PROFILE_MODULE = 'accounts.UserProfile'  # THIS SHOULD BE SET TO PROFILE MODEL

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
    'django.contrib.auth.context_processors.auth',
    'allauth.account.context_processors.account',
    'allauth.socialaccount.context_processors.socialaccount',
)

#==============================================================================
# Middleware
#==============================================================================

MIDDLEWARE_CLASSES += (
    'django.contrib.sessions.middleware.SessionMiddleware',
)

#==============================================================================
# Auth / security
#==============================================================================

AUTHENTICATION_BACKENDS += (
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
    'lazysignup.backends.LazySignupBackend',
    'phileo.auth_backends.CanLikeBackend',
)

#FACEBOOK_REGISTRATION_BACKEND = 'django_facebook.registration_backends.UserenaBackend'

ADAPTOR_INPLACEEDIT_EDIT = 'inplaceeditform.perms.AdminDjangoPermEditInline'


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
#EMAIL_BACKEND = 'django.core.mail.backends.console'
MANDRILL_API_KEY = '60fd0151-320e-433c-8f97-d21d5f9ad96d'
MANDRILL_API_URL = 'http://mandrillapp.com/api/1.0'

#==============================================================================
# Facebook Settings - Production
#==============================================================================
#FACEBOOK_APP_ID = "559089214107050"
#FACEBOOK_APP_SECRET = "a6976d28267f98ef3474f5398ebc6e42"

#==============================================================================
# Miscellaneous project settings
#==============================================================================

CRISPY_TEMPLATE_PACK = 'bootstrap'

if os.getenv('JENKINS_URL', False):
    INSTALLED_APPS += ('django_jenkins', )
    PROJECT_APPS = ('django.contrib.auth', 'django.contrib.contenttypes', 'django.contrib.sessions', 'django.contrib.sites', 'django.contrib.syndication', 'django.contrib.messages', 'django.contrib.staticfiles', 'django.contrib.admin', 'django.contrib.admindocs', 'meals', 'util', 'easy_maps', 'django_facebook', 'crispy_forms', 'friends', 'friends.contrib.suggestions', 'notification', 'launchpad', 'accounts', 'djrill', 'mptt', 'compressor', 'allauth', 'djcelery')
    # DATABASES['default'].update(dict(
    #     ENGINE=os.getenv('DBA_SQL_DJANGO_ENGINE'),
    #     USER=os.getenv('DBA_SQL_ADMIN'),
    #     PASSWORD=os.getenv('DBA_SQL_ADMIN_PASSWORD'),
    #     HOST=os.getenv('DBA_SQL_HOST'),
    #     PORT=os.getenv('DBA_SQL_PORT'),
    # ))

ACTSTREAM_SETTINGS = {
    'MODELS': ('auth.user', 'auth.group', 'comments.comment', 'accounts.usercontact', 'accounts.userprofile', 'meals.meal', 'meals.invite', 'meals.guest'),
    #'MANAGER': 'myapp.streams.MyActionManager',
    'FETCH_RELATIONS': True,
    'USE_PREFETCH': True,
    #'USE_JSONFIELD': True,
}


#==============================================================================
# Third party app settings
#==============================================================================

