# myapp/urls.py
from django.urls import path
from .views import events_api

urlpatterns = [
    path('events/', events_api),
]
