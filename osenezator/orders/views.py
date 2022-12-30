#from django.shortcuts import render

from rest_framework import viewsets
from .models import Order
from .serializers import OrderSerializer
from django_filters.rest_framework import DjangoFilterBackend

class OrderViewSet(viewsets.ModelViewSet):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['driver',]