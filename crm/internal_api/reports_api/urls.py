from django.urls import include, path
from rest_framework import routers

from .views import ReportViewSet

router = routers.SimpleRouter()
router.register(r'reports', ReportViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
