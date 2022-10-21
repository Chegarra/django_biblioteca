from .base import *
from os import environ
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': environ.get('DATABASES_NAME'),
        'USER': environ.get('DATABASES_USER'),
        'PASSWORD': environ.get('DATABASES_PASSWORD'),
        'HOST': environ.get('DATABASES_HOST'),
        'PORT': str(environ.get('DATABASES_PORT'))
    }
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = '/static/'
# STATICFILES_DIR = [BASE_DIR / 'static']
STATICFILES_DIRS = [BASE_DIR.child('static')]