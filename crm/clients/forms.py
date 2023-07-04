from addresses.forms import AddressModelChoiceFromListField
from dal import autocomplete
from django import forms

from .models import Client


class ClientForm(forms.ModelForm):
    address = AddressModelChoiceFromListField(create=True)
    class Meta:
        model = Client
        fields = ('__all__')
        widgets = {
            'company': autocomplete.ModelSelect2(url='company-autocomplete'),
        }

class ClientInlineForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ('__all__')
        widgets = {
            'company': autocomplete.ModelSelect2(url='company-autocomplete'),
        }