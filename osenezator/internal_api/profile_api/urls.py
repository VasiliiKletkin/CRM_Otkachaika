from django.urls import include, path
from rest_framework import routers

from .views import ProfileViewSet

router = routers.SimpleRouter()
router.register(r'profile', ProfileViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
