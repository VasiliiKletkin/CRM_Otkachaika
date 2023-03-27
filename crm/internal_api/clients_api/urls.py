from django.urls import path

from .views import AddressAutocomplete, CityAutocomplete, StreetAutocomplete, RegionAutocomplete, CountryAutocomplete

urlpatterns = [
     path('country-autocomplete/', CountryAutocomplete.as_view(),
         name='country-autocomplete'),
     path('region-autocomplete/', RegionAutocomplete.as_view(),
         name='region-autocomplete'),
     path('city-autocomplete/', CityAutocomplete.as_view(),
         name='city-autocomplete'),
     path('street-autocomplete/', StreetAutocomplete.as_view(),
         name='street-autocomplete'),
     path('address-autocomplete/', AddressAutocomplete.as_view(),
         name='address-autocomplete'),
]
