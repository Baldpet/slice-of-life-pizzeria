from django.contrib import admin
from .models import Offer

# Register your models here.


class OfferAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'item1',
        'item2',
        'item3',
        'deal_price',
    )


admin.site.register(Offer, OfferAdmin)
