from django import forms
from .models import Offer

from crispy_forms.helper import FormHelper, Layout
from crispy_forms.layout import Fieldset, Div, HTML, ButtonHolder, Submit

class OfferForm(forms.ModelForm):
    class Meta:
        model = Offer
        exclude = ['original_price', 'saving']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.template_pack = 'bootstrap4'
        self.helper.form_id = 'add_offer_form'
        self.helper.form_method = 'post'
        self.helper.form_action = 'add_offer'
        self.helper.layout = Layout(
            Fieldset('',
                     Div('name', css_class="m-3"),
                     Div('description', css_class="m-3"),
                     Div(Div('item1', css_class="col-12 col-md-6 m-3 item-selector"),
                         Div('item1_size', css_class="col-12 col-md-4 m-3 item-size"),
                         css_class="row"
                         ),
                     Div(css_class="item1-error"),
                     Div(Div('item2', css_class="col-12 col-md-6 m-3 item-selector"),
                         Div('item2_size', css_class="col-12 col-md-4 m-3 item-size"),
                         css_class="row"
                         ),
                     Div(css_class="item2-error"),
                     Div(Div('item3', css_class="col-12 col-md-6 m-3 item-selector"),
                         Div('item3_size', css_class="col-12 col-md-4 m-3 item-size"),
                         css_class="row"
                         ),
                     Div(css_class="item3-error"),
                     Div('deal_price', css_class="m-3"),
                     Div('image', css_class="m-3"),
                     ),
            ButtonHolder(
                Submit('submit', 'Add Offer',
                       css_class='btn btn-primary m-3')
            ),
        )
