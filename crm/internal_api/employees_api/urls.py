from django.urls import include, path
from rest_framework import routers

from .views import DriverAutocomplete


router = routers.SimpleRouter()


urlpatterns = [
    path('', include(router.urls)),
    path('driver-autocomplete/', DriverAutocomplete.as_view(),
         name='driver-autocomplete'),
]
