import os
import environ

from .common import *  # noqa

env = environ.Env()
environ.Env.read_env()

SECRET_KEY = env('SECRET_KEY', default='r@%v8+&+*ara2(y_b+!r1=&!damzf!s_rp^%_t#vdvkio)(_p$')

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': env('DJANGO_DB_NAME', default='postgres'),
        'HOST': env('DJANGO_DB_HOST', default='db'),
        'USER': env('DJANGO_DB_USER', default='postgres'),
        'PORT': env('DJANGO_DB_PORT', default='5432'),
        'PASSWORD': env('DJANGO_DB_PASSWORD', default='postgres'),
        'ATOMIC_REQUESTS': True,
    },
}
