from rest_framework import viewsets
from .models import Driver
from .serializers import DriverSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import LimitOffsetPagination

class DriverViewSet(viewsets.ModelViewSet):
    queryset = Driver.objects.all()
    serializer_class = DriverSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['telegram_id',]
    pagination_class = LimitOffsetPagination
