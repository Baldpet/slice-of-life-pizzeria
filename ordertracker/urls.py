from django.urls import path
from . import views

urlpatterns = [
    path('', views.order_tracker, name='ordertracker'),
    path('order_status', views.order_status, name='order_status'),
]
