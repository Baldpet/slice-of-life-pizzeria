from django.shortcuts import render

# Create your views here.


def offers(request):
    return render(request, 'offers/offers.html')