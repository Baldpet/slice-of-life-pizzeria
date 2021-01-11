from django.shortcuts import render, get_object_or_404
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
    template = 'offers/offers_detail.html'
    context = {
        'offer': offer
    }
    return render(request, template, context)
