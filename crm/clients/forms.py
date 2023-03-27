from dal import autocomplete
from django import forms

from .models import Address


class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ('__all__')
        widgets = {
            'city': autocomplete.ModelSelect2(url='city-autocomplete'),
            'street': autocomplete.ModelSelect2(url='street-autocomplete'),
        }
