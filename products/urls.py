from django.urls import path
from . import views

urlpatterns = [
    path('pizza', views.pizza, name='pizza'),
]