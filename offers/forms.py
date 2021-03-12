from django import forms
from .models import Offer
from products.models import Category


class OfferForm(forms.ModelForm):
    item1 = forms.ModelChoiceField(
        queryset=Category.objects.exclude(name='Custom'))
    item2 = forms.ModelChoiceField(
        queryset=Category.objects.exclude(name='Custom'), required=False)
    item3 = forms.ModelChoiceField(
        queryset=Category.objects.exclude(name='Custom'), required=False)

    class Meta:
        model = Offer
        exclude = ['original_price', 'saving']
