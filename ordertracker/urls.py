from django.urls import path
from . import views

urlpatterns = [
    path('', views.orderTracker, name='ordertracker'),
]
