import uuid
from django.db import models
from django.db.models import Sum

from django_countries.fields import CountryField

from profiles.models import UserProfile
from products.models import Product, Price

# Create your models here.


class Order(models.Model):
    order_status_choices = [
        ('OP', 'Order placed'),
        ('PR', 'Preparing'),
        ('C', 'Cooking'),
        ('OD', 'Out for delivery'),
    ]

    order_number = models.CharField(max_length=32, null=False, editable=False)
    user_profile = models.ForeignKey(UserProfile, on_delete=models.SET_NULL, null=True, related_name='orders')
    full_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    country = CountryField(blank_label='Country *', null=False, blank=False)
    postcode = models.CharField(max_length=20, null=True, blank=False)
    town_or_city = models.CharField(max_length=40, null=False, blank=True)
    street_address1 = models.CharField(max_length=80, null=False, blank=False)
    street_address2 = models.CharField(max_length=80, null=True, blank=True)
    county = models.CharField(max_length=80, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    order_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
    loyalty_discount = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
    deal_discount = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
    grand_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
    loyalty_points = models.IntegerField()
    order_status = models.CharField(max_length=2, choices=order_status_choices, default='OP')
    original_bag = models.TextField(null=False, blank=False, default='')
    stripe_pid = models.CharField(max_length=254, null=False, blank=False, default='')

    def _generate_order_number(self):
        """
        Generate a random, unique order number using UUID
        """
        return uuid.uuid4().hex.upper()

    def update_total(self):
        """
        Update the grand total each time a line is added
        """
        self.order_total = self.lineitems.aggregate(Sum('lineitem_total'))['lineitem_total__sum'] or 0
        self.grand_total = self.order_total - self.loyalty_discount - self.deal_discount
        self.save()

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the order number
        if it hasn't been set already.
        """
        if not self.order_number:
            self.order_number = self._generate_order_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.order_number


class OrderLineItem(models.Model):
    order = models.ForeignKey(Order, null=False, blank=False, on_delete=models.CASCADE, related_name='lineitems')
    product = models.ForeignKey(Product, null=False, blank=False, on_delete=models.CASCADE)
    product_size = models.CharField(max_length=2, null=True, blank=True)    # XS, S, M, L, XL
    quantity = models.IntegerField(null=False, blank=False, default=0)
    lineitem_total = models.DecimalField(max_digits=6, decimal_places=2, null=False, blank=False, editable=False)

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the lineitem total
        and update the order total.
        """
        product_category = product.category.name
        product_premium = product.is_premium
        price = Price.objects.filter(is_premium=product_premium, category__name=product_category)

        self.lineitem_total = price.price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.product.name} on order {self.order.order_number}'
