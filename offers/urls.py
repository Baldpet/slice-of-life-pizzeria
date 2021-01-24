from django.urls import path
from . import views

urlpatterns = [
    path('', views.offers, name='offers'),
    path('offer/<int:offerId>/', views.offers_detail, name='offers_detail'),
    path('offer_to_bag/<int:offerId>/', views.add_offer_to_bag, name='add_offer_to_bag'),
    path('add_offer/', views.add_offer, name='add_offer'),
]