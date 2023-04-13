from dal import autocomplete
from django import forms

from .models import Client


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ('__all__')
        widgets = {
            'address': autocomplete.ModelSelect2(url='address-autocomplete', attrs={'data-minimum-input-length': 3}),
            'company': autocomplete.ModelSelect2(url='company-autocomplete', attrs={'data-minimum-input-length': 3}),
        }

class ClientInlineForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ('__all__')
        widgets = {
            'company': autocomplete.ModelSelect2(url='company-autocomplete', attrs={'data-minimum-input-length': 3}),
        }