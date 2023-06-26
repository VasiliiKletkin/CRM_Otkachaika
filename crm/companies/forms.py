from dal import autocomplete
from django import forms

from .models import Company, CompanyAccounting, CompanyWorkPlace


class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ('__all__')


class CompanyWorkPlaceInlineForm(forms.ModelForm):
    class Meta:
        model = CompanyWorkPlace
        fields = ('__all__')
        widgets = {
            'countries': autocomplete.ModelSelect2Multiple(url='country-autocomplete'),
            'regions': autocomplete.ModelSelect2Multiple(url='region-autocomplete', forward=["countries"]),
            'cities': autocomplete.ModelSelect2Multiple(url='city-autocomplete', forward=["regions"]),
            'streets': autocomplete.ModelSelect2Multiple(url='street-autocomplete', forward=["cities"]),
        }


class CompanyAccountingInlineForm(forms.ModelForm):
    class Meta:
        model = CompanyAccounting
        fields = ('__all__')


# class SubscriptionsCompanyForm(forms.ModelForm):
#     class Meta:
#         model = SubscriptionCompany
#         fields = ('__all__')
#         widgets = {
#             'company': autocomplete.ModelSelect2(url='company-autocomplete'),
#             'service': autocomplete.ModelSelect2(url='servicecompany-autocomplete'),
#         }