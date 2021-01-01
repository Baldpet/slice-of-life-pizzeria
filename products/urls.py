from django.urls import path
from . import views

urlpatterns = [
    path('pizza', views.pizza, name='pizza'),
    path('sides', views.sides_drinks, name='sides'),
]