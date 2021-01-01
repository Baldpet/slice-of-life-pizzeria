from django.shortcuts import render
from .models import Product, Price
from .forms import MiniForm

# Create your views here.


def pizza(request):
    products = Product.objects.all().filter(category__name='Pizza')
    price = Price.objects.filter(is_premium=False, category__name='Pizza')
    price_premium = Price.objects.filter(is_premium=True,
                                         category__name='Pizza')
    form = MiniForm
    template = 'products/pizza.html'
    context = {
        'products': products,
        'price': price,
        'price_premium': price_premium,
        'form': form,
    }
    return render(request, template, context)


def sides_drinks(request):
    sides = Product.objects.filter(category__name='Side')
    drinks = Product.objects.filter(category__name='Drink')
    price = Price.objects.filter(is_premium=False, category__name='Side')
    price_premium = Price.objects.filter(is_premium=True,
                                         category__name='Side')
    price_drink = Price.objects.filter(is_premium=False,
                                       category__name='Drink')
    price_premium_drink = Price.objects.filter(is_premium=True,
                                               category__name='Drink')
    template = 'products/sides.html'
    context = {
        'sides': sides,
        'drinks': drinks,
        'price': price,
        'price_premium': price_premium,
        'price_drink': price_drink,
        'price_premium_drink': price_premium_drink,
    }
    return render(request, template, context)
