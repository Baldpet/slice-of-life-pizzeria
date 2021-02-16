from django.contrib import admin
from .models import Product, Category, Price, Dough, Sauce, Cheese, Toppings

# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'category',
        'is_premium',
        'image',
    )


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'is_pizza',
        'has_sizes',
    )


class DoughAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'price'
    )

class SauceAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )

class CheeseAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )

class ToppingsAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'price',
    )


class PriceAdmin(admin.ModelAdmin):
    list_display = (
        'category',
        'size',
        'is_premium',
        'price',
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Price, PriceAdmin)
admin.site.register(Dough, DoughAdmin)
admin.site.register(Sauce, SauceAdmin)
admin.site.register(Cheese, CheeseAdmin)
admin.site.register(Toppings, ToppingsAdmin)
