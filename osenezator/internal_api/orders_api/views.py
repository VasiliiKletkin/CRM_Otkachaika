from django.shortcuts import get_object_or_404
from django.utils.timezone import now
from django_filters.rest_framework import DjangoFilterBackend
from orders.models import Order
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response

from .serializers import OrderSerializer


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.order_by('date_created')
    serializer_class = OrderSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['driver',]
    pagination_class = LimitOffsetPagination

    @action(detail=True)
    def started(self, request, pk=None):
        order = get_object_or_404(Order, pk=pk)
        order.status = Order.CANCELED
        order.save()
        return Response({'status': order.CANCELED})

    @action(detail=True)
    def completed(self, request, pk=None):
        order = get_object_or_404(Order, pk=pk)
        order.status = Order.COMPLETED
        order.save()
        return Response({'status': order.status})

    @action(detail=True)
    def canceled(self, request, pk=None):
        order = get_object_or_404(Order, pk=pk)
        order.status = Order.CANCELED
        order.save()
        return Response({'status': order.CANCELED})

    @action(detail=False)
    def today(self, request, *args, **kwargs):
        company_id = request.GET.get('company_id')
        current_datetime = now
        orders = Order.objects.filter(company_id=company_id, date_planned__year=current_datetime.year,
                                      date_planned__month=current_datetime.month, date_planned__day=current_datetime.day)
        return Response({'status': orders})
