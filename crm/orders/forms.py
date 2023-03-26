from clients.models import Address
from dal import autocomplete
from django import forms
from employees.models import Driver
from companies.models import Company

from .models import Order


class OrderForm(forms.ModelForm):
    driver = forms.ModelChoiceField(
        queryset=Driver.objects.all(),
        widget=autocomplete.ModelSelect2(url='driver-autocomplete'), required=False
    )
    address = forms.ModelChoiceField(
        queryset=Address.objects.all(),
        widget=autocomplete.ModelSelect2(url='address-autocomplete')
    )
    company = forms.ModelChoiceField(
        queryset=Company.objects.all(),
        widget=autocomplete.ModelSelect2(url='company-autocomplete'), required=False
    )

    class Meta:
        model = Order
        fields = ('__all__')
        widgets = {
          'description': forms.Textarea(attrs={'rows':2, 'cols':100}),
        }
