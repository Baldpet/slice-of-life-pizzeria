from django.shortcuts import render, get_object_or_404, redirect
from django.shortcuts import reverse, HttpResponse
from django.views.decorators.http import require_POST
from django.conf import settings
from django.contrib import messages

from .forms import OrderForm
from .models import Order, OrderLineItem
from products.models import Product
from profiles.models import UserProfile
from profiles.forms import UserForm

from bag.context import bag_contents

from decimal import Decimal

import stripe
import json

# Create your views here.


@require_POST
def cache_checkout_data(request):
    """
    Caches the data from the order and then add the extra info needed
    for recreating the order through the web hook into the Stripe metadata
    """
    try:
        current_bag = bag_contents(request)
        discount = current_bag['offer_discount']
        pid = request.POST.get('client_secret').split('_secret')[0]
        stripe.api_key = settings.STRIPE_SECRET_KEY
        stripe.PaymentIntent.modify(pid, metadata={
            'username': request.user,
            'save_info': request.POST.get('save-info'),
            'bag': json.dumps(request.session.get('bag', {})),
            'discount': discount,
            'loyalty_points': 0,
        })
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, 'Sorry, your payment cannot be \
            processed right now. Please try again later')
        return HttpResponse(content=e, status=400)


def checkout(request):
    """
    On GET request:
    Renders the checkout page

    On POST:
    Handles the checkout logic through Stripe
    Checks the form validation of checkout
    Adds the relevant loyalty points for the order is logged in
    Saves the client information if requested
    """
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY
    current_bag = bag_contents(request)

    if request.method == 'POST':
        bag = request.session.get('bag', {})
        deal_discount = request.session.get('discount', {})

        form_data = {
            'full_name': request.POST['full_name'],
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],
            'postcode': request.POST['postcode'],
            'town_or_city': request.POST['town_or_city'],
            'street_address1': request.POST['street_address1'],
            'street_address2': request.POST['street_address2'],
            'county': request.POST['county'],
        }

        order_form = OrderForm(form_data)
        if order_form.is_valid():
            order = order_form.save(commit=False)
            pid = request.POST.get('client_secret').split('_secret')[0]
            order.stripe_pid = pid
            order.original_bag = json.dumps(bag)
            order.deal_discount = current_bag['offer_discount']
            loyalty = current_bag['loyalty_discount']
            if not loyalty:
                l_discount = Decimal(0)
            else:
                l_discount = Decimal(loyalty)
            order.loyalty_discount = l_discount
            if request.user.is_authenticated:
                loyalty_points = round(int(current_bag['grand_total'] / 4)) - round(l_discount)
                order.loyalty_points = loyalty_points
            else:
                order.loyalty_points = 0
            order.save()
            for item_id, item_data in bag.items():
                try:
                    product = Product.objects.get(id=item_id)
                    if isinstance(item_data, int):
                        order_line_item = OrderLineItem(
                            order=order,
                            product=product,
                            quantity=item_data
                        )
                        order_line_item.save()
                    else:
                        for dough in item_data.items():
                            for size in dough[1]:
                                if dough[1][size] > 0:
                                    order_line_item = OrderLineItem(
                                        order=order,
                                        product=product,
                                        quantity=dough[1][size],
                                        product_size=size
                                    )
                                    order_line_item.save()
                except Product.DoesNotExist:
                    messages.error(request, "One of the products does not exist.")
                    order.delete()
                    return redirect(reverse('view_bag'))

            request.session['save_info'] = 'save-info' in request.POST
            return redirect(reverse('checkout_success', args=[order.order_number]))
        else:
            messages.error(request, 'There was an error with your form.')

    total = current_bag['grand_total']
    stripe_total = round(total * 100)
    stripe.api_key = stripe_secret_key
    intent = stripe.PaymentIntent.create(
        amount=stripe_total,
        currency=settings.STRIPE_CURRENCY,
    )
    if request.user.is_authenticated:
        try:
            profile = UserProfile.objects.get(user=request.user)
            form = OrderForm(initial={
                'full_name': profile.user.get_full_name(),
                'email': profile.user.email,
                'phone_number': profile.default_phone_number,
                'postcode': profile.default_postcode,
                'town_or_city': profile.default_town_or_city,
                'street_address1': profile.default_street_address1,
                'street_address2': profile.default_street_address2,
                'county': profile.default_county,
            })
        except UserProfile.DoesNotExist:
            form = OrderForm()
    else:
        form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'form': form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret
    }

    return render(request, template, context)


def checkout_success(request, order_number):
    """
    Handle successful checkouts
    """
    order = get_object_or_404(Order, order_number=order_number)
    order_id = order.id
    line_items = OrderLineItem.objects.filter(order=order_id)
    save_info = request.session.get('save_info')

    if request.user.is_authenticated:
        profile = UserProfile.objects.get(user=request.user)
        order.user_profile = profile
        profile.loyalty_points += order.loyalty_points
        profile.save()
        order.save()

        if save_info:
            profile_data = {
                'default_phone_number': order.phone_number,
                'default_postcode': order.postcode,
                'default_town_or_city': order.town_or_city,
                'default_street_address1': order.street_address1,
                'default_street_address2': order.street_address2,
                'default_county': order.county,
            }
            user_profile_form = UserForm(profile_data, instance=profile)
            if user_profile_form.is_valid():
                user_profile_form.save()

    if 'bag' in request.session:
        del request.session['bag']
    if 'discount' in request.session:
        del request.session['discount']
    if 'loyalty' in request.session:
        del request.session['loyalty']

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'line_items': line_items,
    }

    return render(request, template, context)


def pizza_tracker(request, order_number):
    """ Renders the pizza tracker view """
    order = get_object_or_404(Order, order_number=order_number)
    template = 'checkout/pizza_tracker.html'
    context = {
        'order': order
    }

    return render(request, template, context)


def account(request):
    """ Renders the checkout account page """
    template = 'checkout/account.html'
    context = {

    }
    return render(request, template, context)


def update_delivery_or_collection(request):
    """ API to update the delivery or collection option for the customer """
    if request.method == 'POST':
        delivery_or_collection = request.GET.get('delivery')
        request.session['delivery'] = delivery_or_collection
        return HttpResponse(status=200)
    else:
        return HttpResponse(status=400)
