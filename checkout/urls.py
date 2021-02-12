from django.urls import path
from . import views

urlpatterns = [
    path('', views.checkout, name='checkout'),
    path('checkout_success/<order_number>', views.checkout_success, name='checkout_success'),
    path('pizza_tracker/<order_number>', views.pizza_tracker, name='pizza_tracker'),
    path('update_delivery_or_collection/', views.update_delivery_or_collection, name='update_delivery_or_collection'),
]