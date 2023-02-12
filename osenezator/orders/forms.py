from dal import autocomplete
from django import forms
from clients.models import Address
from employees.models import Driver
from .models import Order

class OrderForm(forms.ModelForm):
    driver = forms.ModelChoiceField(
        queryset=Driver.objects.all(),
        widget=autocomplete.ModelSelect2(url='driver-autocomplete')
    )
    address = forms.ModelChoiceField(
        queryset=Address.objects.all(),
        widget=autocomplete.ModelSelect2(url='address-autocomplete')
    )

    class Meta:
        model = Order
        fields = ('__all__')