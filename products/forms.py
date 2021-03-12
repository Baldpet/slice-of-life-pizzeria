from django import forms
from .models import Product, Toppings, Category


class ProductForm(forms.ModelForm):
    toppings = forms.ModelMultipleChoiceField(
            queryset=Toppings.objects.all(),
            required=False,
            widget=forms.CheckboxSelectMultiple)
    category = forms.ModelChoiceField(
        queryset=Category.objects.exclude(name='Custom'))

    class Meta:
        model = Product
        fields = '__all__'
