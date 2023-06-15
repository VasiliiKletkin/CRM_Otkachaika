from django.urls import path

from .views import ClientAutocomplete

urlpatterns = [
    path(
        "client-autocomplete/", ClientAutocomplete.as_view(), name="client-autocomplete"
    ),
]
