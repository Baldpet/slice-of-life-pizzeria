from django import forms
from .models import Product

from crispy_forms.helper import FormHelper, Layout
from crispy_forms.layout import Fieldset, Div, HTML, ButtonHolder, Submit


class MiniForm(forms.Form):
    dough_choices = Product.dough_choices
    dough = forms.ChoiceField(choices=dough_choices)

    dough.widget.attrs['class'] = 'form-control pizza-mini-form'
    dough.label = False


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.template_pack = 'bootstrap4'
        self.helper.form_id = 'add_product_form'
        self.helper.form_method = 'post'
        self.helper.form_action = 'add_product'
        self.helper.layout = Layout(
            Fieldset( '',
                Div('name', css_class="m-3"),
                Div('category', css_class="m-3"),
                Div(
                    HTML("<h4>Base Options</h4>"),
                    css_class="row m-3 text-center pizza-only"
                ),
                Div('dough', css_class="m-3 pizza-only"),
                Div(css_class="pizza_error_div_dough"),
                Div('sauce', css_class="m-3 pizza-only"),
                Div(css_class="pizza_error_div_sauce"),
                Div('cheese', css_class="m-3 pizza-only"),
                Div(css_class="pizza_error_div_cheese"),
                Div(
                    HTML("<h4>Additional Toppings</h4>"),
                    css_class="row m-3 text-center pizza-only"
                ),
                Div(
                    Div('chicken', css_class="col-6 col-md-3"),
                    Div('pepperoni', css_class="col-6 col-md-3"),
                    Div('bacon', css_class="col-6 col-md-3"),
                    Div('sausage', css_class="col-6 col-md-3"),
                    css_class="row mt-3 m-md-3 pizza-only"
                ),
                Div(
                    Div('ham', css_class="col-6 col-md-3"),
                    Div('meatball', css_class="col-6 col-md-3"),
                    Div('chorizo', css_class="col-6 col-md-3"),
                    Div('mushroom', css_class="col-6 col-md-3"),
                    css_class="row m-md-3 pizza-only"
                ),
                Div(
                    Div('pepper', css_class="col-6 col-md-3"),
                    Div('onion', css_class="col-6 col-md-3"),
                    Div('chilli', css_class="col-6 col-md-3"),
                    Div('pineapple', css_class="col-6 col-md-3"),
                    css_class="row m-md-3 pizza-only"
                ),
                Div(
                    Div('key_lime', css_class="col-6 col-md-3"),
                    Div('extra_cheese', css_class="col-6 col-md-3"),
                    css_class="row mb-3 m-md-3 pizza-only"
                ),
                Div('description', css_class="m-3"),
                Div(
                    HTML("<h4>Price</h4>"),
                    css_class="row m-3 text-center"
                ),
                Div('is_premium', css_class="m-3"),
                Div(
                    HTML("<p>Product Price:</p>"),
                    css_class="product_price"
                ),
                Div('image', css_class="m-3"),
            ),
            ButtonHolder(
                Submit('submit', 'Add Product', css_class='btn btn-primary m-3')
            )
        )
