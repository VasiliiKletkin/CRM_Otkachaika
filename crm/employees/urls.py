from django.urls import path

from .views import CarAutocomplete, DriverAutocomplete

urlpatterns = [
    path('driver-autocomplete/', DriverAutocomplete.as_view(),
         name='driver-autocomplete'),
    path('car-autocomplete/', CarAutocomplete.as_view(),
         name='car-autocomplete'),
]