from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .models import Product, Price, Dough, Toppings, Cheese, Sauce
from .forms import ProductForm

# Create your views here.


def pizza(request):
    products = Product.objects.all().filter(category__name='Pizza', is_original=True)
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
    if request.method == 'POST':
        form = ProductForm(request.POST)
        form.price = 0
        form.is_original = True
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Successfully added the product')
            return redirect(reverse('product_management'))
        else:
            print('error')
            messages.error(request, 'Failed to add the offer.')
    else:
        print('test')
        form = ProductForm

    pizza_price = Price.objects.filter(category__name='Pizza')
    side_price = Price.objects.filter(category__name='Side')
    drink_price = Price.objects.filter(category__name='Drink')
    toppings = Toppings.objects.all()

    template = 'products/add_product.html'
    context = {
        'form': form,
        'pizza_price': pizza_price,
        'side_price': side_price,
        'drink_price': drink_price,
        'toppings': toppings
    }

    return render(request, template, context)


def create_a_pizza(request):
    custom_size = Price.objects.filter(category__name='Custom')
    dough = Dough.objects.all()
    cheese = Cheese.objects.all()
    sauce = Sauce.objects.all()
    toppings = Toppings.objects.all()

    if request.method == 'POST':
        bag = request.session.get('bag', {})
        product = Product()
        product.name = 'Custom Pizza'
        product.category_id = 1
        product.dough = Dough(request.POST.get('dough'))
        product.cheese = Cheese(request.POST.get('cheese'))
        product.sauce = Sauce(request.POST.get('sauce'))
        product.is_original = False
        product.price = 0
        product.description = 'Custom Pizza'
        product.save()
        if request.POST.get('toppings'):
            product.toppings.set(request.POST.getlist('toppings'))
        item_id = product.id
        quantity = 1
        size = request.POST.get('size')
        dough_id = request.POST.get('dough')
        dough_queryset = Dough.objects.filter(id=dough_id)
        dough = str(dough_queryset[0]).lower()
        if item_id in list(bag.keys()):
            messages.success(request, f'Added ({product.name} - {dough.capitalize()} - {size}) to your order.')
            bag[item_id][dough][size] += quantity
        else:
            bag[item_id] = {'classic': {'S': 0,
                                        'M': 0,
                                        'L': 0,
                                        'XL': 0,
                                        },
                            'thin': {'S': 0,
                                    'M': 0,
                                    'L': 0,
                                    'XL': 0,
                                    },
                            'stuffed': {'S': 0,
                                        'M': 0,
                                        'L': 0,
                                        'XL': 0,
                                        },
                            }
            messages.success(request, f'Added ({product.name} - {dough.capitalize()} - {size}) to your order.')
            bag[item_id][dough][size] = quantity

        request.session['bag'] = bag

        return redirect('pizza')

    template = 'products/create_a_pizza.html'
    context = {
        'size': custom_size,
        'dough': dough,
        'cheese': cheese,
        'sauce': sauce,
        'toppings': toppings
    }

    return render(request, template, context)
