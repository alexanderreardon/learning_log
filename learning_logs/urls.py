"""Defines URL patterns for learning_logs."""

from django.conf.urls import url
from . import views

app_name = 'Learning Logs'

urlpatterns = [
    # Home page
    url(r'^$', views.index, name='index'),
]
