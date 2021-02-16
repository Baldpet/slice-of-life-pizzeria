from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .models import Product, Price, Dough
from .forms import ProductForm

# Create your views here.


def pizza(request):
    products = Product.objects.all().filter(category__name='Pizza')
    price = Price.objects.filter(is_premium=False, category__name='Pizza')
    price_premium = Price.objects.filter(is_premium=True,
                                         category__name='Pizza')
    dough = Dough.objects.all()
    template = 'products/pizza.html'
    context = {
        'products': products,
        'price': price,
        'price_premium': price_premium,
        'dough': dough,
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


def add_product(request):
    pizza_price = Price.objects.filter(category__name='Pizza')
    side_price = Price.objects.filter(category__name='Side')
    drink_price = Price.objects.filter(category__name='Drink')
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Successfully added the product')
            return redirect(reverse('product_management'))
        else:
            messages.error(request, 'Failed to add the offer.')
    else:
        form = ProductForm

    template = 'products/add_product.html'
    context = {
        'form': form,
        'pizza_price': pizza_price,
        'side_price': side_price,
        'drink_price': drink_price,
    }

    return render(request, template, context)
