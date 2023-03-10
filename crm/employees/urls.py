from django.urls import path

from .views import DriverAutocomplete

urlpatterns = [
    path('driver-autocomplete/', DriverAutocomplete.as_view(),
         name='driver-autocomplete'),
]
