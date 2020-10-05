"""
Our main urls
"""
from django.conf import settings
from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('apps.api.urls')),
]
