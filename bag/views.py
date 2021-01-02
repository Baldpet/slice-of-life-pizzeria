from django.shortcuts import render, get_object_or_404, redirect
from products.models import Product

# Create your views here.


def view_bag(request):
    """ View the current bag contents """
    bag = request.session.get('bag', {})
    print(bag)
    return render(request, 'bag/bag.html')


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
    print(bag)
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
