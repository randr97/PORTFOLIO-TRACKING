import os
import environ
import dj_database_url

from decouple import config

from .common import *  # noqa

SECRET_KEY = config('SECRET_KEY')

DEBUG = config('DEBUG', default=True)

DATABASES = {
    'default': dj_database_url.config(
        default=config('DATABASE_URL')
    )
}

db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_env)

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')  # noqa
STATIC_URL = '/static/'

# Extra places for collectstatic to find static files.
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),  # noqa
)

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
