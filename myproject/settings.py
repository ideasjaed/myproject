# Django settings for myproject project.  
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
     ('Jazmin', 'ideas.jaed@gmail.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),                  # Or path to database file if using sqlite3.
        'USER': '',
        'PASSWORD': '',
        'HOST': '',                      # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '',                      # Set to empty string for default.
    }
}

# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
ALLOWED_HOSTS = ['jaed.webfactional.com','www.sistemacesic.com']

TIME_ZONE = 'UTC'

LANGUAGE_CODE = 'es-MX'

SITE_ID = 1

USE_I18N = True

USE_L10N = True

USE_TZ = True

MEDIA_ROOT = '/home/jaed/webapps/static_media/carga'

MEDIA_URL = '/media/'

STATIC_ROOT = '/home/jaed/webapps/static_media'

STATIC_URL = '/static/'

STATICFILES_DIRS = ( os.path.join( BASE_DIR, 'myproject/static'),

    )

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

SECRET_KEY = '#vv2=@ynlm#%%$bu707ph82zi+$ky^s4f5ub(1d4qw-z6hal+4'

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    'django.template.loaders.eggs.Loader',
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

ROOT_URLCONF = 'myproject.urls'

EMAIL_USE_TLS=True
EMAIL_HOST='smtp.gmail.com'
EMAIL_HOST_USER='sistemacesic@gmail.com'
EMAIL_HOST_PASSWORD='chio1234'
EMAIL_PORT=587

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'myproject.wsgi.application'

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR,'myproject/plantillas'),
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
    'front',
    'saed',
)

SESSION_SERIALIZER = 'django.contrib.sessions.serializers.JSONSerializer'

LOGIN_REDIRECT_URL = '/login/'

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
