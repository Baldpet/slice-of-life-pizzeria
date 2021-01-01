from django.shortcuts import render, get_object_or_404, redirect
from products.models import Product

# Create your views here.


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
