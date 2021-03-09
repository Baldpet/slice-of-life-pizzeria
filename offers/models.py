from django.db import models
from products.models import Category, Price
from django.db.models.signals import pre_save
from django.dispatch import receiver
from decimal import Decimal

# Create your models here.


class Offer(models.Model):
    size_choices = [
        ('NA', 'Non Applicable'),
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
        ('XL', 'Extra-Large')
    ]

    name = models.CharField(max_length=254, null=False, blank=False)
    description = models.TextField()
    item1 = models.ForeignKey(Category, related_name='Category_item1', null=False,
                              blank=False, on_delete=models.CASCADE)
    item1_size = models.CharField(max_length=2, choices=size_choices,
                                  null=True, blank=True, default='NA')
    item2 = models.ForeignKey(Category, related_name='Category_item2', null=True,
                              blank=True, on_delete=models.SET_NULL)
    item2_size = models.CharField(max_length=2, choices=size_choices,
                                  null=True, blank=True, default='NA')
    item3 = models.ForeignKey(Category, related_name='Category_item3', null=True,
                              blank=True, on_delete=models.SET_NULL)
    item3_size = models.CharField(max_length=2, choices=size_choices,
                                  null=True, blank=True, default='NA')
    original_price = models.DecimalField(max_digits=6, decimal_places=2, default=Decimal(0))
    deal_price = models.DecimalField(max_digits=6, decimal_places=2)
    saving = models.DecimalField(max_digits=6, decimal_places=2, default=Decimal(0))
    image = models.ImageField(upload_to='images/', null=False, blank=False)

    def __str__(self):
        return self.name

    def calculate_saving(self):
        """
        Calculates the total potential saving of the deal
        and store it as a value in the model to use later

        Uses the original price (calculated) and the
        deal price (supplied at the time of saving)
        """
        self.saving = self.original_price - self.deal_price

    def original_price_calculation(self):
        """
        Calculates the highest price of each item in the deal
        and adds these together to get a total original price
        for the items included in the deal.
        """
        pizza_price = Price.objects.all().filter(category__name='Pizza',
                                                 is_premium='True')
        side_price = Price.objects.all().filter(category__name='Side',
                                                is_premium='True')
        drink_price = Price.objects.all().filter(category__name='Drink',
                                                 is_premium='True')

        def item_choice(item, size):
            if item == 'Side':
                print('Im a side')
                return side_price[0].price
            elif item == 'Drink':
                print('Im a side')
                return drink_price[0].price
            elif item is None:
                print('Im nothing')
                return 0
            else:
                pizza_price_size = pizza_price.filter(size=size)
                return pizza_price_size[0].price

        item1_price = item_choice(self.item1.name, self.item1_size)
        if self.item2 is not None:
            item2_price = item_choice(self.item2.name, self.item2_size)
        else:
            item2_price = 0
        if self.item3 is not None:
            item3_price = item_choice(self.item3.name, self.item3_size)
        else:
            item3_price = 0

        self.original_price = item1_price + item2_price + item3_price
