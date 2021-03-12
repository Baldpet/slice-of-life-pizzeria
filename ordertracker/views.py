from django.shortcuts import render, HttpResponse, get_object_or_404
from django.http import JsonResponse

from checkout.models import Order


def order_tracker(request):
    """ Renders the ordertracker view """
    orders = Order.objects.all().exclude(order_status='D')

    template = 'ordertracker/orders.html'
    context = {
        'orders': orders
    }
    return render(request, template, context)


def order_status(request):
    """
    API for the order tracker to check or update the status
    On GET request:
    Supplies the current status of the order
    On POST request:
    Updates the database with the new order status
    """
    if request.method == 'POST':
        order_id = request.GET.get('orderId')
        status = request.GET.get('status')
        order = get_object_or_404(Order, id=order_id)
        order.order_status = status
        order.save()
        return HttpResponse(status=200)
    elif request.method == 'GET':
        order_id = request.GET.get('orderId')
        order = get_object_or_404(Order, id=order_id)
        data = {
            'status': order.order_status
        }
        return JsonResponse(data)
