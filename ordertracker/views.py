from django.shortcuts import render

from checkout.models import Order, OrderLineItem


def order_tracker(request):
    orders = Order.objects.all().exclude( order_status='D')

    template = 'ordertracker/orders.html'
    context = {
        'orders': orders
    }
    return render(request, template, context)
