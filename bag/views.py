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


def add_side_to_bag(request, item_id):
    """ Add a side or a drink to the current bag """

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    price = request.POST.get('price')
    bag = request.session.get('bag', {})

    if item_id in list(bag.keys()):
        new_quantity = bag[item_id][0]
        new_quantity += quantity
        bag[item_id] = new_quantity, price
    else:
        bag[item_id] = quantity, price

    request.session['bag'] = bag

    return redirect(redirect_url)
