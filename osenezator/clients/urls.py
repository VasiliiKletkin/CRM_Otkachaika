from django.urls import path
from .views import AddressAutocomplete 

urlpatterns = [
    path('address-autocomplete/', AddressAutocomplete.as_view(),name='address-autocomplete'),
]
