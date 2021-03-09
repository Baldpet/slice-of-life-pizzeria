from django import forms
from .models import Product, Toppings


from crispy_forms.helper import FormHelper, Layout
from crispy_forms.layout import Fieldset, Div, HTML, ButtonHolder, Submit


class ProductForm(forms.ModelForm):
    toppings = forms.ModelMultipleChoiceField(
            queryset=Toppings.objects.all(),
            widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = Product
        fields = '__all__'
