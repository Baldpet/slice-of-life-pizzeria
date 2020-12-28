from django.shortcuts import render

# Create your views here.


def pizza(request):
    template = 'products/pizza.html'
    context = {

    }
    return render(request, template, context)
