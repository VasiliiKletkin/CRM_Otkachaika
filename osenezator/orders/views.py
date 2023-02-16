#from django.shortcuts import render

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.pagination import LimitOffsetPagination
from django.shortcuts import get_object_or_404
from rest_framework.response import Response

from .models import Order
from .serializers import OrderSerializer


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.order_by('date_created')
    serializer_class = OrderSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['driver',]
    pagination_class = LimitOffsetPagination

    @action(detail=True)
    def canseled(self, request, pk=None):
        order = get_object_or_404(Order, pk=pk)
        order.status=Order.CANCELED
        order.save()
        return Response({'status': order.CANCELED})
    
   
    @action(detail=True)
    def completed(self, request, pk=None):
        order = get_object_or_404(Order, pk=pk)
        order.status=Order.COMPLETED
        order.save()
        return Response({'status': order.status})
    
    @action(detail=True)
    def canseled(self, request, pk=None):
        order = get_object_or_404(Order, pk=pk)
        order.status=Order.CANCELED
        order.save()
        return Response({'status': order.CANCELED})
    
