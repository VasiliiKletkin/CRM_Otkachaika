from dal import autocomplete
from django import forms

from .models import (AccountingCompany, Company, SubscriptionCompany,
                     WorkPlaceCompany)


class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ('__all__')


class WorkPlaceCompanyInlineForm(forms.ModelForm):
    class Meta:
        model = WorkPlaceCompany
        fields = ('__all__')
        widgets = {
            'countries': autocomplete.ModelSelect2Multiple(url='country-autocomplete'),
            'regions': autocomplete.ModelSelect2Multiple(url='region-autocomplete', forward=["countries"]),
            'cities': autocomplete.ModelSelect2Multiple(url='city-autocomplete', forward=["regions"]),
            'streets': autocomplete.ModelSelect2Multiple(url='street-autocomplete', forward=["cities"]),
        }


class AccountingCompanyInlineForm(forms.ModelForm):
    class Meta:
        model = AccountingCompany
        fields = ('__all__')


class SubscriptionsCompanyForm(forms.ModelForm):
    class Meta:
        model = SubscriptionCompany
        fields = ('__all__')
        widgets = {
            'company': autocomplete.ModelSelect2(url='company-autocomplete'),
            'service': autocomplete.ModelSelect2(url='servicecompany-autocomplete'),
        }