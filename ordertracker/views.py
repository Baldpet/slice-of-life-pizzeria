from django.shortcuts import render, HttpResponse, get_object_or_404

from checkout.models import Order, OrderLineItem


def order_tracker(request):
    orders = Order.objects.all().exclude( order_status='D')

    template = 'ordertracker/orders.html'
    context = {
        'orders': orders
    }
    return render(request, template, context)


def order_status(request):
    if request.method == 'POST':
        order_id = request.GET.get('orderId')
        status = request.GET.get('status')
        order = get_object_or_404(Order, id=order_id)
        order.order_status = status
        order.save()
        return HttpResponse(status=200)
