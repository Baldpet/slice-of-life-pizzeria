from django.shortcuts import render, get_object_or_404, redirect, HttpResponse, reverse
from django.contrib import messages

from .models import Offer
from .forms import OfferForm
from products.models import Product, Price

from decimal import Decimal

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


def add_offer(request):
    if request.method == 'POST':
        form = OfferForm(request.POST)
        if form.is_valid():
            offer = form.save()
            messages.success(request, 'Successfully added the product')
            return redirect(reverse('product_management'))
        else:
            messages.error(request, 'Failed to add the offer.')
    else:
        form = OfferForm

    template = 'offers/add_offer.html'
    context = {
        'form': form,
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
    if 'item2' in request.POST:
        item2_id = request.POST.get('item2')
        item2_quantity = 1
        product2 = get_object_or_404(Product, pk=item2_id)
        item2Exists = True
        if product2.category.has_sizes:
            item2_size = request.POST.get('item2_size')
            item2_dough = request.POST.get('item2_dough')
    else:
        item2Exists = False
        item2_id = ""
    if 'item3' in request.POST:
        item3_id = request.POST.get('item3')
        item3_quantity = 1
        item3Exists = True
        product3 = get_object_or_404(Product, pk=item3_id)
        if product3.category.has_sizes:
            item3_size = request.POST.get('item3_size')
            item3_dough = request.POST.get('item3_dough')
    else:
        item3Exists = False
        item3_id = ""
    bag = request.session.get('bag', {})
    discount = request.session.get('discount', {})
    total_cost = 0
    deal = offer.deal_price
    try:
        if product1.category.name == 'Pizza':
            add_offer_pizza(bag, item1_id, item1_dough, item1_size, item1_quantity)
            if product1.is_premium:
                price_object = get_object_or_404(Price, is_premium=True, size=item1_size)
                price = price_object.price
                total_cost += price
            else:
                price_object = get_object_or_404(Price, is_premium=False, size=item1_size)
                price = price_object.price
                total_cost += price
        else:
            add_offer_other(bag, item1_id, item1_quantity)
            if product1.is_premium:
                price_object = get_object_or_404(Price, category__name=product1.category.name, is_premium=True)
                price = price_object.price
                total_cost += price
            else:
                price_object = get_object_or_404(Price, category__name=product1.category.name, is_premium=False)
                price = price_object.price
                total_cost += price
        if item2Exists:
            if product2.category.name == 'Pizza':
                add_offer_pizza(bag, item2_id, item2_dough, item2_size, item2_quantity)
                if product2.is_premium:
                    price_object = get_object_or_404(Price, is_premium=True, size=item2_size)
                    price = price_object.price
                    total_cost += price
                else:
                    price_object = get_object_or_404(Price, is_premium=False, size=item2_size)
                    price = price_object.price
                    total_cost += price
            else:
                add_offer_other(bag, item2_id, item2_quantity)
                if product2.is_premium:
                    price_object = get_object_or_404(Price, category__name=product2.category.name, is_premium=True)
                    price = price_object.price
                    total_cost += price
                else:
                    price_object = get_object_or_404(Price, category__name=product2.category.name, is_premium=False)
                    price = price_object.price
                    total_cost += price
        if item3Exists:
            if product3.category.name == 'Pizza':
                add_offer_pizza(bag, item3_id, item3_dough, item3_size, item3_quantity)
                if product3.is_premium:
                    price_object = get_object_or_404(Price, is_premium=True, size=item3_size)
                    price = price_object.price
                    total_cost += price
                else:
                    price_object = get_object_or_404(Price, is_premium=False, size=item3_size)
                    price = price_object.price
                    total_cost += price
            else:
                add_offer_other(bag, item3_id, item3_quantity)
                if product3.is_premium:
                    price_object = get_object_or_404(Price, category__name=product3.category.name, is_premium=True)
                    price = price_object.price
                    total_cost += price
                else:
                    price_object = get_object_or_404(Price, category__name=product3.category.name, is_premium=False)
                    price = price_object.price
                    total_cost += price
        messages.success(request, f'Added {offer.name} to your order.')
    except Exception as e:
        messages.error(request, f'Error removing item: {e}.')
        return HttpResponse(status=500)

    discount_amount = str(total_cost - deal)
    discount[offerId] = {
        'items': [item1_id, item2_id, item3_id],
        'discount': discount_amount,
    }

    request.session['bag'] = bag
    request.session['discount'] = discount

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
