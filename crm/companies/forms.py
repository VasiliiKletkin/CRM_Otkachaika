from dal import autocomplete
from django import forms

from .models import Company, SubscriptionCompany


class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ('__all__')
        widgets = {
            'country': autocomplete.ModelSelect2(url='country-autocomplete'),
            'cities': autocomplete.ModelSelect2Multiple(url='city-autocomplete', forward=["country"]),
            'streets': autocomplete.ModelSelect2Multiple(url='street-autocomplete', forward=["cities"]),
        }

class SubscriptionsCompanyForm(forms.ModelForm):
    class Meta:
        model = SubscriptionCompany
        fields = ('__all__')
        widgets = {
            'company': autocomplete.ModelSelect2(url='company-autocomplete'),
            'service': autocomplete.ModelSelect2(url='servicecompany-autocomplete'),
        }