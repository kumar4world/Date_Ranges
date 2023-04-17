from charset_normalizer import api
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
]
