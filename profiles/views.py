from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .forms import UserForm
from .models import UserProfile

from offers.models import Offer
from offers.forms import OfferForm
from products.models import Product, Price, Toppings
from products.forms import ProductForm

# Create your views here.


def profile(request):
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')
        else:
            messages.error(request, 'Update failed. Please ensure the form is valid.')
    else:
        form = UserForm(instance=profile)

    template = 'profiles/profile.html'
    context = {
        'form': form,
        'profile': profile,
    }
    return render(request, template, context)


def product_management(request):
    offers = Offer.objects.all()
    products = Product.objects.all().order_by('category')

    template = 'profiles/product_management.html'
    context = {
        'offers': offers,
        'products': products,
    }

    return render(request, template, context)


def amend_product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    if request.method == "POST":
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Product successfully updated.')
            return redirect('product_management')
        else:
            messages.success(request, 'Product failed to update.')
    else:
        form = ProductForm(instance=product)

    pizza_price = Price.objects.filter(category__name='Pizza')
    side_price = Price.objects.filter(category__name='Side')
    drink_price = Price.objects.filter(category__name='Drink')
    toppings = Toppings.objects.all()

    template = 'profiles/amend_product.html'
    context = {
        'form': form,
        'pizza_price': pizza_price,
        'side_price': side_price,
        'drink_price': drink_price,
        'toppings': toppings,
        'product': product,
    }

    return render(request, template, context)


def amend_offer(request, offer_id):
    offer = get_object_or_404(Offer, pk=offer_id)
    if request.method == "POST":
        form = OfferForm(request.POST, instance=offer)
        if form.is_valid():
            form.save()
            messages.success(request, 'Offer successfully updated.')
            return redirect('product_management')
        else:
            messages.success(request, 'Offer failed to update.')
    else:
        form = OfferForm(instance=offer)
    template = 'profiles/amend_offer.html'
    context = {
        'form': form,
        'offer': offer,
    }

    return render(request, template, context)


def delete_product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Product successfully deleted.')
    return redirect('product_management')


def delete_offer(request, offer_id):
    offer = get_object_or_404(Offer, pk=offer_id)
    offer.delete()
    messages.success(request, 'Offer successfully deleted.')
    return redirect('product_management')
