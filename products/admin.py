from django.contrib import admin
from .models import Product, Category, Price

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


class PriceAdmin(admin.ModelAdmin):
    list_display = (
        'category',
        'is_premium',
        'price',
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Price, PriceAdmin)
