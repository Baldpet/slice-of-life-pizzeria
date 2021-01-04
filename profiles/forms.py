from django import forms
from .models import UserProfile


class UserForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ('user', 'loyalty_points', )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        labels = {
            'default_phone_number': 'Phone Number',
            'default_street_address1': 'Address',
            'default_street_address2': '',
            'default_town_or_city': 'Town or City',
            'default_county': 'County',
            'default_postcode': 'Postcode',
            'default_country': 'Country',
        }

        self.fields['default_phone_number'].widget.attrs['autofocus'] = True
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
            self.fields[field].label = labels[field]
