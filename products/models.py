from django.db import models

# Create your models here.


class Price(models.Model):
    size_choices = [
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
        ('XL', 'Extra-Large')
    ]
    category = models.ForeignKey('Category', null=True,
                                 blank=True, on_delete=models.SET_NULL)
    size = models.CharField(max_length=2, choices=size_choices,
                            null=True, blank=True)
    is_premium = models.BooleanField(default=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return f'{self.category} / {self.size}'


class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254, null=True, blank=True)
    is_pizza = models.BooleanField(default=False, null=True, blank=True)
    has_sizes = models.BooleanField(default=False, null=True, blank=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    dough_choices = [
        ('classic', 'Classic'),
        ('thin', 'Thin'),
        ('stuffed', 'Stuffed'),
    ]
    sauce_choices = [
        ('tomato', 'tomato'),
        ('bbq', 'bbq'),
        ('garlic', 'garlic'),
    ]
    cheese_choices = [
        ('mozzarella', 'mozzarella'),
        ('cheddar', 'cheddar'),
        ('vegan', 'vegan'),
    ]
    name = models.CharField(max_length=254, null=True, blank=True)
    category = models.ForeignKey('Category', null=True,
                                 blank=True, on_delete=models.SET_NULL)
    dough = models.CharField(max_length=254, choices=dough_choices,
                             default='classic', null=True, blank=True)
    sauce = models.CharField(max_length=254, choices=sauce_choices,
                             default='tomato', null=True, blank=True)
    cheese = models.CharField(max_length=254,
                              choices=cheese_choices,
                              default='mozzarella', null=True, blank=True)
    chicken = models.BooleanField(default=False, null=True, blank=True)
    pepperoni = models.BooleanField(default=False, null=True, blank=True)
    bacon = models.BooleanField(default=False, null=True, blank=True)
    sausage = models.BooleanField(default=False, null=True, blank=True)
    ham = models.BooleanField(default=False, null=True, blank=True)
    meatball = models.BooleanField(default=False, null=True, blank=True)
    chorizo = models.BooleanField(default=False, null=True, blank=True)
    mushroom = models.BooleanField(default=False, null=True, blank=True)
    pepper = models.BooleanField(default=False, null=True, blank=True)
    onion = models.BooleanField(default=False, null=True, blank=True)
    chilli = models.BooleanField(default=False, null=True, blank=True)
    pineapple = models.BooleanField(default=False, null=True, blank=True)
    key_lime = models.BooleanField(default=False, null=True, blank=True)
    extra_cheese = models.BooleanField(default=False, null=True, blank=True)
    description = models.TextField()
    is_premium = models.BooleanField(default=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name
