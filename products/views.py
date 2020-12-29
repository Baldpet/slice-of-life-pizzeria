from django.shortcuts import render
from .models import Product, Price

# Create your views here.


def pizza(request):
    products = Product.objects.all().filter(category__name='Pizza')
    price = Price.objects.all()
    template = 'products/pizza.html'
    context = {
        'products': products,
        'price': price,
    }
    return render(request, template, context)
