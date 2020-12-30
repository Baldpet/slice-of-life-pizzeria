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
