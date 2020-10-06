import os
import environ
import dj_database_url

from decouple import config

from .common import *  # noqa

SECRET_KEY = config('SECRET_KEY')

DEBUG = config('DEBUG', default=False)

DATABASES = {
    'default': dj_database_url.config(
        default=config('DATABASE_URL')
    )
}

db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_env)

STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'
