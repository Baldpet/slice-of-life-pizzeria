from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserForm
from .models import UserProfile

from offers.models import Offer
from offers.forms import OfferForm
from products.models import Product, Price, Toppings
from products.forms import ProductForm

# Create your views here.


def profile(request):
    """
    Renders the user profile page.
    """
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')
        else:
            messages.error(request,
                           'Update failed. Please ensure the form is valid.')
    else:
        form = UserForm(instance=profile)

    template = 'profiles/profile.html'
    context = {
        'form': form,
        'profile': profile,
    }
    return render(request, template, context)


def product_management(request):
    """
    Renders the product management page
    """
    offers = Offer.objects.all()
    products = Product.objects.all().order_by('category')

    template = 'profiles/product_management.html'
    context = {
        'offers': offers,
        'products': products,
    }

    return render(request, template, context)


@login_required
def amend_product(request, product_id):
    """
    Renders the amend product form with the relevant product info already input
    On POST of the form it will update the same product and redirect
    to product management page
    """

    if not request.user.is_superuser:
        messages.error(request, 'Sorry only store owners can do that.')
        return redirect(reverse('home'))

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


@login_required
def amend_offer(request, offer_id):
    """
    Renders the amend offer form with the inputs already updated
    for the relevant offer
    On POST will update the offer and save with the new info and
    redirect to product management
    """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry only store owners can do that.')
        return redirect(reverse('home'))

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


@login_required
def delete_product(request, product_id):
    """
    Deletes the selected product from the database
    """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Product successfully deleted.')
    return redirect('product_management')


@login_required
def delete_offer(request, offer_id):
    """
    Deletes the selected offer from the database
    """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry only store owners can do that.')
        return redirect(reverse('home'))

    offer = get_object_or_404(Offer, pk=offer_id)
    offer.delete()
    messages.success(request, 'Offer successfully deleted.')
    return redirect('product_management')
