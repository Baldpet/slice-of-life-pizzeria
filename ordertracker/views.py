from django.shortcuts import render


def orderTracker(request):
    template = 'ordertracker/orders.html'
    context = {

    }
    return render(request, template, context)
