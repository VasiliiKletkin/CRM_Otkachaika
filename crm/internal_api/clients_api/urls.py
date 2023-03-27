from django.urls import path

from .views import AddressAutocomplete, CitiesAutocomplete, StreetAutocomplete

urlpatterns = [
    path('address-autocomplete/', AddressAutocomplete.as_view(),
         name='address-autocomplete'),
    path('city-autocomplete/', CitiesAutocomplete.as_view(),
         name='city-autocomplete'),
    path('street-autocomplete/', StreetAutocomplete.as_view(),
         name='street-autocomplete'),
]
