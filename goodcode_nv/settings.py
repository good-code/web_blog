# Django settings for goodcode_nv project.
import os
FORCE_SCRIPT_NAME=""
DEBUG = True
APPEND_SLASH = False
TEMPLATE_DEBUG = DEBUG
THUMBNAIL_DEBUG = TEMPLATE_DEBUG
THUMBNAIL_EXTENSION = 'png'
THUMBNAIL_ENGINE = 'sorl.thumbnail.engines.pil_engine.Engine'

ADMINS = (
     ('Arek', 'arek@goodcode.co.uk'),
)

MANAGERS = ADMINS
DIRNAME = os.path.join(__file__)
DATABASES = {
        'default': { 'ENGINE': 'django.db.backends.postgresql_psycopg2', 'NAME':  'goodcode', 'USER': 'fireant', 'PASSWORD':'Data_13'},       
        #'default' : { 'ENGINE': 'django.db.backends.sqlite3', 'NAME':  '/home/fireant/goodcode_nv/goodcode.db'},
        #'bkp' : { 'ENGINE': 'django.db.backends.sqlite3', 'NAME':  '/home/fireant/goodcode_nv/goodcode_bk.db'},
        }
SITE_URL = 'http://goodcode.co.uk'

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'Europe/London'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-gb'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = '/home/fireant/image-server/'

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
MEDIA_URL = 'http://images.goodcode.co.uk/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
STATIC_ROOT = '/home/fireant/image-server/static/'

# URL prefix for static files.
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'xytu538f^l%p&amp;g$0yx+o6%=r3jot9g2u=sh8(s%8dff5@dib-0'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'goodcode_nv.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'goodcode_nv.wsgi.application'

TEMPLATE_DIRS = (
   '/home/arek/projects/goodcode_nv/goodcode_nv/templates/',
)
TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'goodcode_nv.context_processors.add_fortune',
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'django.contrib.admindocs',
    'django.contrib.comments',
    'reversion',
    'django.contrib.markup',
    'goodcode_nv',
    'goodcode_nv.photographs',
    'django_comments_xtd',
    'sorl.thumbnail',
)

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}
COMMENTS_XTD_CONFIRM_EMAIL = True
COMMENTS_APP = "django_comments_xtd"
LATEST_ALBUMS_NR=4
