from addresses.utils import get_or_create_address, get_address
from dal import autocomplete
from django import forms

from .models import Address


class AddressForm(forms.ModelForm):
    # def clean(self):
    #     home = self.cleaned_data['home']
    #     street = self.cleaned_data['street']
    #     if Address.objects.filter(street_id=street, home=home).exists():
    #         raise forms.ValidationError('Такой адрес уже существует')
    #     self.cleaned_data['home'] = self.cleaned_data['home'].upper()
    #     return super().clean()

    class Meta:
        model = Address
        fields = ('__all__')



class AddressModelChoiceFromListField(forms.ModelChoiceField):

    def __init__(self, create=False, *args, **kwargs):
        self.create = create
        kwargs['widget'] = autocomplete.ListSelect2(url='dadata-address-autocomplete')
        kwargs['queryset'] = Address.objects.all()
        super().__init__(*args, **kwargs)

    def clean(self, value):
        try:
            value = get_or_create_address(value) if self.create else get_address(value)
            return super().clean(value)
        except Exception:
            raise forms.ValidationError("Невозможно выбрать данный адрес")
