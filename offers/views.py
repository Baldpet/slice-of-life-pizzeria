from django.shortcuts import render, get_object_or_404
from .models import Offer
from products.models import Product
from products.forms import MiniForm

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
