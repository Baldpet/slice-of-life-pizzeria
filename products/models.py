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

    name = models.CharField(max_length=254, null=False, blank=False)
    is_pizza = models.BooleanField(default=False, null=True, blank=True)
    has_sizes = models.BooleanField(default=False, null=True, blank=True)

    def __str__(self):
        return self.name


class Dough(models.Model):
    name = models.CharField(max_length=254, null=False, blank=False)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.name


class Sauce(models.Model):
    name = models.CharField(max_length=254, null=False, blank=False)

    def __str__(self):
        return self.name


class Cheese(models.Model):
    name = models.CharField(max_length=254, null=False, blank=False)

    def __str__(self):
        return self.name


class Toppings(models.Model):
    name = models.CharField(max_length=254, null=False, blank=False)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=254, null=False, blank=False)
    category = models.ForeignKey('Category', null=False,
                                 blank=False, on_delete=models.CASCADE)
    dough = models.ForeignKey('Dough', null=True,
                                 blank=True, on_delete=models.SET_NULL)
    sauce = models.ForeignKey('Sauce', null=True,
                                 blank=True, on_delete=models.SET_NULL)
    cheese = models.ForeignKey('Cheese', null=True,
                                 blank=True, on_delete=models.SET_NULL)
    toppings = models.ManyToManyField('Toppings', blank=True)
    description = models.TextField()
    is_premium = models.BooleanField(default=True)
    is_original = models.BooleanField(default=True)
    image = models.ImageField(upload_to='images/', null=True, blank=True)

    def __str__(self):
        return self.name
