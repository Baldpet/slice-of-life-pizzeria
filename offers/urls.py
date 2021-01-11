from django.urls import path
from . import views

urlpatterns = [
    path('', views.offers, name='offers'),
    path('offer/<int:offerId>/', views.offers_detail, name='offers_detail'),
]