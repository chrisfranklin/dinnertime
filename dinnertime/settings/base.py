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
TIME_ZONE = 'Europe/London'
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

DEFAULT_FROM_EMAIL = 'TableSurfin <info@tablesurf.in>'

# Make this unique, and don't share it with anybody.
SECRET_KEY = 's^tsuf-^w*w&amp;&amp;)#-_9xh2l8r$qs4itiq8h1a2aft&amp;rjj^7#9aj'

INSTALLED_APPS = (
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
    'accounts',
    'meals',
    'util',
    'easy_maps',
    'rest_framework',
    'rest_framework.authtoken',
    'autocomplete_light',
    'django_gravatar',
    'crispy_forms',
    'friends',
    'oauth_access',
    'friends.contrib.suggestions',
    'notification',
    'launchpad',
    #--------------------------------------------------------------------------
    # Util
    #--------------------------------------------------------------------------
    'djrill',
    'mptt',
    'compressor',
    'djcelery',
    'django_statsd',
    'app_metrics',
    'raven.contrib.django',
    #'reversion',
    'south',

    'django_gravatar',  # added but not tested, warning may mess with the line below
    'avatar', # we do not need two avatar packages TODO: which avatar package should we use.
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.facebook',
    'allauth.socialaccount.providers.google',
    # 'allauth.socialaccount.providers.github',
    'allauth.socialaccount.providers.linkedin',
    # 'allauth.socialaccount.providers.openid',
    # 'allauth.socialaccount.providers.persona',
    # 'allauth.socialaccount.providers.soundcloud',
    'allauth.socialaccount.providers.twitter',

    #'django_basic_feedback',
    'inplaceeditform',
    'actstream',
    'phileo',
    'yummly',
    'cities_light',
    'gunicorn',

)

# For raven and ultimately sentry
SENTRY_DSN = "https://280631656bac415cbf5eeeebd4c3e94b:10f7d01657dd4a4dad2b7bb32c68b31f@app.getsentry.com/4327"

APP_METRICS_BACKEND = 'app_metrics.backends.statsd'

STATSD_CLIENT = 'django_statsd.clients.log'
STATSD_PATCHES = [
        'django_statsd.patches.db',
        'django_statsd.patches.cache',
]
# This next bit is for beacon support, add more keys from the beacon if you wish (yahoo beacon)
STATSD_RECORD_KEYS = [
        'window.performance.timing.domComplete',
        'window.performance.timing.domInteractive',
        'window.performance.timing.domLoading',
        'window.performance.navigation.redirectCount',
        'window.performance.navigation.type',
]

PHILEO_LIKABLE_MODELS = {

    "meals.Meal": {},  # can override default config settings for each model here
    "actstream.Action": {},
    "meals.Part": {}

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
LOGIN_URL = '/accounts/login/'
LOGOUT_URL = '/accounts/logout/'
ANONYMOUS_USER_ID = -1

AUTH_PROFILE_MODULE = 'accounts.UserProfile'  # THIS SHOULD BE SET TO PROFILE MODEL

STATIC_URL = '/static/'
MEDIA_URL = '/uploads/'

STATIC_ROOT = os.path.join(VAR_ROOT, 'static')
MEDIA_ROOT = os.path.join(VAR_ROOT, 'uploads')

STATICFILES_DIRS = (
    os.path.join(PROJECT_DIR, 'static'),
)

FIXTURE_DIRS += ('%s/fixtures/prod' % PROJECT_DIR,)

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
    'django_statsd.middleware.GraphiteRequestTimingMiddleware',
    'django_statsd.middleware.GraphiteMiddleware',
)

#==============================================================================
# Auth / security
#==============================================================================

AUTHENTICATION_BACKENDS += (
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
    #'lazysignup.backends.LazySignupBackend',
    'phileo.auth_backends.CanLikeBackend',
)

ACCOUNT_EMAIL_REQUIRED = True

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
    #'MANAGER': 'myapp.streams.MyActionManager',
    #  temporarily removed django.contrib.auth from test due to bug #17966 in django, test cannot be run as it is.
    #  temp remove 'autocomplete_light',
    #  temp remove 'lazysignup','app_metrics',
    #  temp remove 'avatar', 'compressor',
    PROJECT_APPS = ('django.contrib.contenttypes', 'django.contrib.sessions', 'django.contrib.sites', 'django.contrib.syndication', 'django.contrib.messages', 'django.contrib.staticfiles', 'django.contrib.admin', 'django.contrib.admindocs', 'django.contrib.comments', 'meals', 'util', 'easy_maps', 'rest_framework', 'django_gravatar', 'crispy_forms', 'friends', 'oauth_access', 'friends.contrib.suggestions', 'notification', 'launchpad', 'accounts', 'djrill', 'mptt', 'allauth', 'allauth.account', 'allauth.socialaccount', 'allauth.socialaccount.providers.facebook', 'allauth.socialaccount.providers.google', 'allauth.socialaccount.providers.linkedin', 'allauth.socialaccount.providers.twitter', 'djcelery', 'inplaceeditform', 'actstream',  'phileo', 'yummly', 'django_statsd', 'raven.contrib.django')
    # DATABASES['default'].update(dict(
    #     ENGINE=os.getenv('DBA_SQL_DJANGO_ENGINE'),
    #     USER=os.getenv('DBA_SQL_ADMIN'),
    #     PASSWORD=os.getenv('DBA_SQL_ADMIN_PASSWORD'),
    #     HOST=os.getenv('DBA_SQL_HOST'),
    #     PORT=os.getenv('DBA_SQL_PORT'),
    # ))

ACTSTREAM_SETTINGS = {
    'MODELS': ('auth.user', 'auth.group', 'comments.comment', 'accounts.usercontact', 'accounts.userprofile', 'meals.meal', 'meals.invite', 'meals.guest', 'meals.invitee'),
    #'MANAGER': 'myapp.streams.MyActionManager',
    'FETCH_RELATIONS': True,
    'USE_PREFETCH': True,
    #'USE_JSONFIELD': True,
}

YUMMLY_KEY = "9687047d"
YUMMLY_SECRET = "48703203011932335cfaf5fb57ef4f1a"


#==============================================================================
# Third party app settings
#==============================================================================

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    # 'filters': {
    #     'special': {
    #         '()': 'project.logging.SpecialFilter',
    #         'foo': 'bar',
    #     }
    # },
    'handlers': {
        'null': {
            'level': 'DEBUG',
            'class': 'django.utils.log.NullHandler',
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler',
            #'filters': ['special']
        },
        # 'test_statsd_handler': {
        #     'class': 'django_statsd.loggers.errors.StatsdHandler',
        # },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'propagate': True,
            'level': 'INFO',
        },
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': False,
        },
        # 'myproject.custom': {
        #     'handlers': ['console', 'mail_admins'],
        #     'level': 'INFO',
        #     'filters': ['special']
        # }
    }
}
