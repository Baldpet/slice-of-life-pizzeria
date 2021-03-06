from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
from products.models import Product, Price
from django.contrib import messages

from profiles.models import UserProfile

# Create your views here.


def view_bag(request):
    """ View the current bag contents """
    price = Price.objects.filter(is_premium=False, category__name='Pizza')
    price_premium = Price.objects.filter(is_premium=True,
                                         category__name='Pizza')
    if request.user.is_authenticated:
        profile = get_object_or_404(UserProfile, user=request.user)
    else:
        profile = False

    context = {
        'price': price,
        'price_premium': price_premium,
        'profile': profile,
    }
    return render(request, 'bag/bag.html', context)


def amend_bag(request, item_id):
    """ Adjust the bag to the requested quantity and/or size change """
    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    original_size = None
    size = None
    dough = None
    if 'product_size' in request.POST:
        size = request.POST['product_size']
        dough = request.POST['dough']
        original_size = request.POST['original_size']
    bag = request.session.get('bag', {})

    try:
        if size:
            if bag[item_id][dough][size] == 0:
                bag[item_id][dough][original_size] = 0
                bag[item_id][dough][size] = quantity
            else:
                bag[item_id][dough][original_size] = 0
                bag[item_id][dough][size] += quantity
            if original_size == size:
                messages.success(request, f'Amended your order of ({product.name} - {dough.capitalize()} - {size}) to a quantity of {quantity}.')
            else:
                messages.success(request, f'Amended your order to ({product.name} - {dough.capitalize()} - {size}) and a quantity of {quantity}.')
        else:
            messages.success(request, f'Amended your order of {product.name} to a quantity of {quantity}.')
            bag[item_id] = quantity

        discount = request.session.get('discount', {})
        product_str = str(product.id)

        for offer_id, offer_info in discount.items():
            print(offer_info)
            if product_str in offer_info.get('items'):
                discount.pop(offer_id)
                break

        request.session['bag'] = bag

        return redirect('view_bag')

    except Exception as e:
        messages.error(request, f'Error removing item: {e}.')
        return HttpResponse(status=500)


def remove_item_from_bag(request, item_id):
    """ Remove the selected item from the bag """

    try:
        product = get_object_or_404(Product, pk=item_id)
        size = None
        dough = None
        if 'product_size' in request.POST:
            size = request.POST['product_size']
            dough = request.POST['dough']
        bag = request.session.get('bag', {})

        if size:
            messages.success(request, f'Removed ({product.name} - {dough.capitalize()} - {size}) from your order.')
            bag[item_id][dough][size] = 0
        else:
            messages.success(request, f'Removed {product.name} from your order.')
            bag.pop(item_id)

        discount = request.session.get('discount', {})
        product_str = str(product.id)

        for offer_id, offer_info in discount.items():
            print(offer_info)
            if product_str in offer_info.get('items'):
                discount.pop(offer_id)
                break

        request.session['bag'] = bag

        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, f'Error removing item: {e}.')
        return HttpResponse(status=500)


def clear_bag(request):
    """ Clear the bag of all items """

    del request.session['bag']
    if 'discount' in request.session:
        del request.session['discount']
    if 'loyalty' in request.session:
        del request.session['loyalty']
    messages.success(request, 'Removed all items from your order.')
    return render(request, 'bag/bag.html')


def add_pizza_to_bag(request, item_id):
    """ Add a pizza to the current bag """
    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    size = request.POST.get('product_size')
    dough_base = request.POST.get('dough').lower()
    bag = request.session.get('bag', {})

    try:
        if item_id in list(bag.keys()):
            messages.success(request, f'Added ({product.name} - {dough_base.capitalize()} - {size}) to your order.')
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
            messages.success(request, f'Added ({product.name} - {dough_base.capitalize()} - {size}) to your order.')
            bag[item_id][dough_base][size] = quantity

        request.session['bag'] = bag

        return redirect(redirect_url)

    except Exception as e:
        messages.error(request, f'Error adding pizza: {e}.')
        return HttpResponse(status=500)


def add_side_to_bag(request, item_id):
    """ Add a side or a drink to the current bag """

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    try:
        if item_id in list(bag.keys()):
            messages.success(request, f'Added {product.name} to your order.')
            bag[item_id] += quantity
        else:
            messages.success(request, f'Added {product.name} to your order.')
            bag[item_id] = quantity

        request.session['bag'] = bag

        return redirect(redirect_url)

    except Exception as e:
        messages.error(request, f'Error adding item: {e}.')
        return HttpResponse(status=500)


def add_loyalty_discount(request):
    """
        Adds the loyalty discount to the session variable
        and applies the discount to the total
    """
    profile = get_object_or_404(UserProfile, user=request.user)
    try:
        request.session['loyalty'] = '5.00'
        messages.success(request, 'Successfully applied your loyalty discount')
        profile.loyalty_points -= 5
        return redirect('view_bag')
    except:
        messages.error(request, 'Loyalty discount failed to apply to your order')
        return HttpResponse(status=500)


def remove_loyalty_discount(request):
    """
    Removes the loyalty discount from the session variable
    and thus removes the discount from the total
    """
    del request.session['loyalty']
    return redirect('view_bag')
