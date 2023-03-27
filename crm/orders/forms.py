from dal import autocomplete
from django import forms

from .models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('__all__')
        widgets = {
            'driver' : autocomplete.ModelSelect2(url='driver-autocomplete'),
            'address': autocomplete.ModelSelect2(url='address-autocomplete'),
            'company': autocomplete.ModelSelect2(url='company-autocomplete'),
            'description': forms.Textarea(attrs={'rows': 2, 'cols': 125}),
        }
