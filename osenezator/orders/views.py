#from django.shortcuts import render

from rest_framework import viewsets
from .models import Order
from .serializers import OrderSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import LimitOffsetPagination

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['driver',]
    pagination_class = LimitOffsetPagination
