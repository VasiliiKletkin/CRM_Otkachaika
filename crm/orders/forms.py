from dal import autocomplete
from django import forms

from .models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('__all__')
        widgets = {
            'company': autocomplete.ModelSelect2(url='company-autocomplete'),
            'driver': autocomplete.ModelSelect2(url='driver-autocomplete', forward=['company']),
            'address': autocomplete.ModelSelect2(url='address-autocomplete', attrs={'data-minimum-input-length': 3}, forward=['company']),
            'client': autocomplete.ModelSelect2(url='client-autocomplete', forward=['company', 'address']),
            'description': forms.Textarea(attrs={'rows': 2, 'cols': 125}),
        }
