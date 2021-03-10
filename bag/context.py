from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product, Price, Category


def bag_contents(request):

    bag_items = []
    total = 0
    product_count = 0
    bag = request.session.get('bag', {})

    for item_id, item_data in bag.items():
        if isinstance(item_data, int):
            side = get_object_or_404(Category, name='Side')
            drink = get_object_or_404(Category, name='Drink')
            product = get_object_or_404(Product, pk=item_id)
            if product.category.name == 'Side':
                if product.is_premium:
                    price_object = get_object_or_404(Price, is_premium=True, category=side.id)
                    price = price_object.price
                else:
                    price_object = get_object_or_404(Price, is_premium=False, category=side.id)
                    price = price_object.price
            else:
                if product.is_premium:
                    price_object = get_object_or_404(Price, is_premium=True, category=drink.id)
                    price = price_object.price
                else:
                    price_object = get_object_or_404(Price, is_premium=False, category=drink.id)
                    price = price_object.price
            total += item_data * price
            product_count += item_data
            bag_items.append({
                'item_id': item_id,
                'quantity': item_data,
                'product': product,
                'price': price,
            })
        else:
            product = get_object_or_404(Product, pk=item_id)
            pizza = get_object_or_404(Category, name='Pizza')
            custom = get_object_or_404(Category, name='Custom')
            for dough in item_data.items():
                for size in dough[1]:
                    if dough[1][size] > 0:
                        if not product.is_original:
                            if product.is_premium:
                                price_object = get_object_or_404(Price, is_premium=True, category=custom, size=size)
                                toppings = product.toppings.all()
                                topping_count = 0
                                for topping in toppings:
                                    topping_count += 1
                                topping_price = Decimal(topping_count * 0.5)
                                price = price_object.price + topping_price
                        else:
                            if product.is_premium:
                                price_object = get_object_or_404(Price, is_premium=True, category=pizza.id, size=size)
                                price = price_object.price
                            else:
                                price_object = get_object_or_404(Price, is_premium=False, category=pizza.id, size=size)
                                price = price_object.price

                        quantity = dough[1][size]
                        total += quantity * price
                        product_count += quantity
                        bag_items.append({
                            'item_id': item_id,
                            'quantity': quantity,
                            'product': product,
                            'size': size,
                            'price': price,
                            'dough': dough[0],
                        })

    discount = request.session.get('discount', {})
    total_discount = 0

    for offer_id, offer_item in discount.items():
        discount_amount = Decimal(offer_item['discount'])
        total_discount += discount_amount

    loyalty = request.session.get('loyalty', False)
    loyalty_discount = loyalty

    if not loyalty_discount:
        total_loyalty_discount = 0
    else:
        total_loyalty_discount = Decimal(loyalty)

    delivery = 0

    grand_total = delivery + total - total_discount - total_loyalty_discount

    context = {
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'grand_total': grand_total,
        'offer_discount': total_discount,
        'loyalty_discount': loyalty_discount,
        }

    return context
