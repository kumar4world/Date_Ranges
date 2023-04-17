from django.urls import path
from . import views

urlpatterns = [
    path('', views.check_overlap, name='check_overlap'),
]

