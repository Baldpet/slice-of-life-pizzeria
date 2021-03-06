from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_bag, name='view_bag'),
    path('addpizza/<item_id>/', views.add_pizza_to_bag,
         name='add_pizza_to_bag'),
    path('addside/<item_id>/', views.add_side_to_bag, name='add_side_to_bag'),
    path('amend_bag/<item_id>/', views.amend_bag, name='amend_bag'),
    path('remove_item/<item_id>/', views.remove_item_from_bag,
         name='remove_item_from_bag'),
    path('clear_bag/', views.clear_bag, name='clear_bag'),
    path('loyalty_points/add/', views.add_loyalty_discount, name='add_loyalty_discount'),
    path('loyalty_points/remove/', views.remove_loyalty_discount, name='remove_loyalty_discount'),
]
