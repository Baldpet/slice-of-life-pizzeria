from django import template

""" Taken directly from code institute Boutique Ado project """

register = template.Library()


@register.filter(name='calc_subtotal')
def calc_subtotal(price, quantity):
    return quantity * price
