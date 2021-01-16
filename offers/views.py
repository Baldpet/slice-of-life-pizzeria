from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
from django.contrib import messages
from .models import Offer
from products.models import Product

# Create your views here.


def offers(request):
    offers = Offer.objects.all()
    template = 'offers/offers.html'
    context = {
        'offers': offers
    }
    return render(request, template, context)


def offers_detail(request, offerId):
    offer = get_object_or_404(Offer, pk=offerId)
    pizzas = Product.objects.all().filter(category__name='Pizza')
    sides = Product.objects.all().filter(category__name='Side')
    drinks = Product.objects.all().filter(category__name='Drink')
    dough_choices = Product.dough_choices
    dough_choices_items = []
    for dough in dough_choices:
        dough_choices_items.append(dough[0])

    template = 'offers/offers_detail.html'
    context = {
        'offer': offer,
        'pizzas': pizzas,
        'sides': sides,
        'drinks': drinks,
        'dough_choices': dough_choices_items,
    }
    return render(request, template, context)


def add_offer_to_bag(request, offerId):
    offer = get_object_or_404(Offer, pk=offerId)
    item1_id = request.POST.get('item1')
    item1_quantity = 1
    product1 = get_object_or_404(Product, pk=item1_id)
    if product1.category.has_sizes:
        item1_size = request.POST.get('item1_size')
        item1_dough = request.POST.get('item1_dough')
    item2_id = request.POST.get('item2')
    item2_quantity = 1
    product2 = get_object_or_404(Product, pk=item2_id)
    if product2.category.has_sizes:
        item2_size = request.POST.get('item2_size')
        item2_dough = request.POST.get('item2_dough')
    item3_id = request.POST.get('item3')
    item3_quantity = 1
    product3 = get_object_or_404(Product, pk=item3_id)
    if product3.category.has_sizes:
        item3_size = request.POST.get('item3_size')
        item3_dough = request.POST.get('item3_dough')
    bag = request.session.get('bag', {})
    try:
        if product1.category.name == 'Pizza':
            add_offer_pizza(bag, item1_id, item1_dough, item1_size, item1_quantity)
        else:
            add_offer_other(bag, item1_id, item1_quantity)
        if product2.category.name == 'Pizza':
            add_offer_pizza(bag, item2_id, item2_dough, item2_size, item2_quantity)
        else:
            add_offer_other(bag, item2_id, item2_quantity)
        if product3.category.name == 'Pizza':
            add_offer_pizza(bag, item3_id, item3_dough, item3_size, item3_quantity)
        else:
            add_offer_other(bag, item3_id, item3_quantity)
        messages.success(request, f'Added {offer.name} to your order.')
    except Exception as e:
        messages.error(request, f'Error removing item: {e}.')
        return HttpResponse(status=500)

    request.session['bag'] = bag

    return redirect('view_bag')


def add_offer_pizza(bag, item_id, dough_base, size, quantity):
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

    return bag


def add_offer_other(bag, item_id, quantity):
    if item_id in list(bag.keys()):
        bag[item_id] += quantity
    else:
        bag[item_id] = quantity

    return bag
