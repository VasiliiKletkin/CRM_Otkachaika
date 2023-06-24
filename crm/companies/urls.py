from django.urls import include, path
from .views import CompanyAutocomplete


urlpatterns = [
    path(
        "company-autocomplete/",
        CompanyAutocomplete.as_view(),
        name="company-autocomplete",
    ),
    # path(
    #     "servicecompany-autocomplete/",
    #     ServiceCompanyAutocomplete.as_view(),
    #     name="servicecompany-autocomplete",
    # ),
]
