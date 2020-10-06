"""
It exposes the WSGI callable as a module-level variable named ``application``.
"""
import os

from whitenoise.django import DjangoWhiteNoise

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.dev")

application = get_wsgi_application()

application = DjangoWhiteNoise(application)
