from django.contrib import admin
from .models import Order, OrderLineItem

# Register your models here.


class OrderLineItemAdminInline(admin.TabularInline):
    model = OrderLineItem
    readonly_fields = ('lineitem_total',)


class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineItemAdminInline,)

    readonly_fields = ('order_number', 'date',
                       'order_total', 'loyalty_discount',
                       'deal_discount', 'grand_total',
                       'original_bag', 'stripe_pid',)

    fields = ('order_number', 'user_profile', 'date',
              'full_name', 'email', 'phone_number',
              'country', 'postcode', 'town_or_city',
              'street_address1', 'street_address2',
              'county', 'order_total',
              'loyalty_discount', 'deal_discount',
              'grand_total', 'order_status', 'loyalty_points',
              'original_bag', 'stripe_pid',
              )

    list_display = ('order_number', 'date', 'full_name', 'order_total',
                    'loyalty_discount', 'deal_discount', 'grand_total',)


admin.site.register(Order, OrderAdmin)
