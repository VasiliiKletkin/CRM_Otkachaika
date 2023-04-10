from dal import autocomplete
from django import forms

from .models import Address, City, Country, Region, Street


class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ('__all__')
        widgets = {
            'city': autocomplete.ModelSelect2(url='city-autocomplete'),
            'street': autocomplete.ModelSelect2(url='street-autocomplete', attrs={'data-minimum-input-length': 3}, forward=['city']),
        }


class RegionForm(forms.ModelForm):
    class Meta:
        model = Region
        fields = ('__all__')
        widgets = {
            'country': autocomplete.ModelSelect2(url='country-autocomplete', attrs={'data-minimum-input-length': 3}),
        }


class CityForm(forms.ModelForm):
    class Meta:
        model = City
        fields = ('__all__')
        widgets = {
            'country': autocomplete.ModelSelect2(url='country-autocomplete'),
            'region': autocomplete.ModelSelect2(url='region-autocomplete', attrs={'data-minimum-input-length': 3},  forward=['country']),
        }


class StreetForm(forms.ModelForm):
    class Meta:
        model = Street
        fields = ('__all__')
        widgets = {
            'city': autocomplete.ModelSelect2(url='city-autocomplete', attrs={'data-minimum-input-length': 3}),
        }
