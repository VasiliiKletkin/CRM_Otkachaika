from dal import autocomplete
from django import forms

from .models import Car


class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ('__all__')
        widgets = {
            'company': autocomplete.ModelSelect2(url='company-autocomplete'),
            'driver': autocomplete.ModelSelect2(url='driver-autocomplete', forward=['company']),
        }


class CarInlineForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ('__all__')
        widgets = {
            'company': autocomplete.ModelSelect2(url='company-autocomplete'),
        }


