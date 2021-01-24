from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile, name='profile'),
    path('product_management', views.product_management, name='product_management'),
]