from rest_framework import viewsets
from .models import Driver
from .serializers import DriverSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import LimitOffsetPagination

class DriverViewSet(viewsets.ModelViewSet):
    serializer_class = DriverSerializer
    queryset = Driver.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['user_telegram_id',]
    pagination_class = LimitOffsetPagination
