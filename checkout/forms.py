from django import forms
from .models import Order

from crispy_forms.helper import FormHelper, Layout
from crispy_forms.layout import Fieldset, Div, HTML, ButtonHolder, Submit

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('full_name', 'email', 'phone_number',
                  'street_address1', 'street_address2',
                  'town_or_city', 'postcode', 'country',
                  'county',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, *kwargs)
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.template_pack = 'bootstrap4'
        
        self.helper.layout = Layout(
            Fieldset( '',
                      Div('full_name', css_class="m-3"),
                      Div('email', css_class="m-3"),
                      Div('phone_number', css_class="m-3"),
                      Div('street_address1', css_class="m-3"),
                      Div('street_address2', css_class="m-3"),
                      Div('town_or_city', css_class="m-3"),
                      Div('county', css_class="m-3"),
                      Div('postcode', css_class="m-3"),
                      Div('country', css_class="m-3"),
            )
        )