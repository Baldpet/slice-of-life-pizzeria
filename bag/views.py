from django.shortcuts import render, get_object_or_404, redirect
from products.models import Product, Price

# Create your views here.


def view_bag(request):
    """ View the current bag contents """
    price = Price.objects.filter(is_premium=False, category__name='Pizza')
    price_premium = Price.objects.filter(is_premium=True,
                                         category__name='Pizza')
    context = {
        'price': price,
        'price_premium': price_premium
    }
    return render(request, 'bag/bag.html', context)


def amend_bag(request, item_id):
    """ Adjust the bag to the requested quantity and/or size change """
    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    original_size = None
    size = None
    dough = None
    if 'product_size' in request.POST:
        size = request.POST['product_size']
        dough = request.POST['dough']
        original_size = request.POST['original_size']
    bag = request.session.get('bag', {})

    if size:
        if bag[item_id][dough][size] == 0:
            bag[item_id][dough][original_size] = 0
            bag[item_id][dough][size] = quantity
        else:
            bag[item_id][dough][original_size] = 0
            bag[item_id][dough][size] += quantity
    else:
        bag[item_id] = quantity

    request.session['bag'] = bag

    return redirect('view_bag')


def clear_bag(request):
    """ Clear the bag of all items """

    del request.session['bag']
    return render(request, 'bag/bag.html')


def add_pizza_to_bag(request, item_id):
    """ Add a pizza to the current bag """
    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    size = request.POST.get('product_size')
    dough_base = request.POST.get('dough')
    bag = request.session.get('bag', {})

    if item_id in list(bag.keys()):
        bag[item_id][dough_base][size] += quantity
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
        bag[item_id][dough_base][size] = quantity

    request.session['bag'] = bag

    return redirect(redirect_url)


def add_side_to_bag(request, item_id):
    """ Add a side or a drink to the current bag """

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if item_id in list(bag.keys()):
        bag[item_id] += quantity
    else:
        bag[item_id] = quantity

    request.session['bag'] = bag

    return redirect(redirect_url)
