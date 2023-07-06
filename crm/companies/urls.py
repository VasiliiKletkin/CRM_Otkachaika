from django.urls import include, path

from .views import CompanyAutocomplete

urlpatterns = [
    path("company-autocomplete/", CompanyAutocomplete.as_view(),
        name="company-autocomplete",
    )
]
