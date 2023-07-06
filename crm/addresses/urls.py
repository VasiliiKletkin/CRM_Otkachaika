from django.urls import path

from .views import AddressAutocomplete, DadataAddressListAutocomplete

urlpatterns = [
    path('address-autocomplete/', AddressAutocomplete.as_view(),
         name='address-autocomplete'),
    path('dadata-address-autocomplete/', DadataAddressListAutocomplete.as_view(),
         name='dadata-address-autocomplete'),
]
