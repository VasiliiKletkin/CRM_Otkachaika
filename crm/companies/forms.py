from dal import autocomplete
from django import forms

from .models import Company


class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ('__all__')
        widgets = {
            'country': autocomplete.ModelSelect2(url='country-autocomplete'),
            'work_of_cities': autocomplete.ModelSelect2Multiple(url='city-autocomplete', forward=["country"]),
        }
