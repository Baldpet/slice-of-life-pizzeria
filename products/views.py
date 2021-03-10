from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required


from .models import Product, Price, Dough, Toppings, Cheese, Sauce
from .forms import ProductForm


# Create your views here.


def pizza(request):
    """
    Renders the pizza page, showing all avaible pizzas to buy
    """
    products = Product.objects.all().filter(category__name='Pizza',
                                            is_original=True)
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
    """
    Renders the sides/drinks page, showing all avaible pizzas to buy
    """
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


@login_required
def add_product(request):
    """
    Adds a product to the database
    """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Successfully added the product')
            return redirect(reverse('product_management'))
        else:
            messages.error(request, 'Failed to add the offer.')
    else:
        form = ProductForm

    pizza_price = Price.objects.filter(category__name='Pizza')
    side_price = Price.objects.filter(category__name='Side')
    drink_price = Price.objects.filter(category__name='Drink')

    template = 'products/add_product.html'
    context = {
        'form': form,
        'pizza_price': pizza_price,
        'side_price': side_price,
        'drink_price': drink_price,
    }

    return render(request, template, context)


def create_a_pizza(request):
    """
    Allows the user to create their own pizza
    Creates the pizza in the products model and uses this for checkout
    The product created has 'is_original' as false
    so that it does not appear elsewhere in the site.
    """
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
            messages.success(request,
                             f'Added ({product.name} - {dough.capitalize()} - {size}) to your order.')
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
            messages.success(request,
                             f'Added ({product.name} - {dough.capitalize()} - {size}) to your order.')
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
