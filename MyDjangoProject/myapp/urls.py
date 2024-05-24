# URL Configuration for the application.
# This module defines the URL patterns for routing the application's views.

from django.urls import path
from .views import display_data

# List of URL patterns handled by this configuration.
# The 'urlpatterns' list routes URLs to views.
urlpatterns = [
    # Maps the 'display/' URL to the 'display_data' view.
    # Users accessing 'http://<domain>/display/' will be served by this view.
    path('display/', display_data, name='display_data'),
]
