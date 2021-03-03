from django.urls import path
from . import views
from .webhooks import webhook

urlpatterns = [
    path('', views.checkout, name='checkout'),
    path('cache_checkout_data/', views.cache_checkout_data, name='cache_checkout_data'),
    path('checkout_success/<order_number>', views.checkout_success, name='checkout_success'),
    path('account', views.account, name='account'),
    path('pizza_tracker/<order_number>', views.pizza_tracker, name='pizza_tracker'),
    path('update_delivery_or_collection/', views.update_delivery_or_collection, name='update_delivery_or_collection'),
    path('wh/', webhook, name='webhook'),
]
