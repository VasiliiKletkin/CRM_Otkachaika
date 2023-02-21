from django.urls import include, path
from rest_framework import routers

from .views import DriverAutocomplete, DriverViewSet


router = routers.SimpleRouter()
router.register(r'drivers', DriverViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('driver-autocomplete/', DriverAutocomplete.as_view(),
         name='driver-autocomplete'),
]
