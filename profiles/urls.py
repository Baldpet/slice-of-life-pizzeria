from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile, name='profile'),
    path('product_management', views.product_management, name='product_management'),
    path('product_amend/<product_id>', views.amend_product, name='amend_product'),
    path('offer_amend/<offer_id>', views.amend_offer, name='amend_offer'),
    path('product_delete/<product_id>', views.delete_product, name='delete_product'),
    path('offer_delete/<offer_id>', views.delete_offer, name='delete_offer'),
]