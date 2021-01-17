from django import forms
from .models import Product


class MiniForm(forms.Form):
    dough_choices = Product.dough_choices
    dough = forms.ChoiceField(choices=dough_choices)

    dough.widget.attrs['class'] = 'form-control pizza-mini-form'
    dough.label = False


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
