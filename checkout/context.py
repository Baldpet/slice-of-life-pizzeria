def delivery_choice(request):
    delivery = request.session['delivery']
    if delivery == 'delivery':
        delivery = True
    else:
        delivery = False

    context = {
        'delivery_choice': delivery,
    }

    return context
