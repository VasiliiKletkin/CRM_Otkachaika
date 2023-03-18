from datetime import datetime

from django.db.models import Q
from django.shortcuts import get_object_or_404
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
    filterset_fields = ('driver', 'company')
    pagination_class = LimitOffsetPagination

    @action(detail=True)
    def inprogress(self, request, pk=None):
        order = get_object_or_404(Order, pk=pk)
        order.status = Order.INPROGRESS
        order.save()
        serializer = self.get_serializer(order)
        return Response(serializer.data)

    @action(detail=True)
    def completed(self, request, pk=None):
        order = get_object_or_404(Order, pk=pk)
        order.status = Order.COMPLETED
        order.save()
        serializer = self.get_serializer(order)
        return Response(serializer.data)

    @action(detail=True)
    def canceled(self, request, pk=None):
        order = get_object_or_404(Order, pk=pk)
        order.status = Order.CANCELED
        order.save()
        serializer = self.get_serializer(order)
        return Response(serializer.data)

    @action(detail=False)
    def today(self, request, *args, **kwargs):
        current_datetime = datetime.today()
        orders = Order.objects.filter(Q(date_planned__date__lte=current_datetime) | Q(
            date_planned__isnull=True), status__in=[Order.CONFIRMED, Order.INPROGRESS], is_showed=False)
        serializer = self.get_serializer(list(orders), many=True)
        orders.update(is_showed=True)
        return Response(serializer.data)

    # def today(self, request, *args, **kwargs):
    #     company_id = request.GET.get('company_id')
    #     current_datetime = datetime.now()
    #     all_today_orders = Order.objects.filter(company_id=company_id, date_planned__year=current_datetime.year,
    #                                             date_planned__month=current_datetime.month, date_planned__day=current_datetime.day,
    #                                             status__in=[Order.CONFIRMED, Order.INPROGRESS]).annotate(sum_orders=Sum('price')).count()

    #     all_today_completed_orders = Order.objects.filter(company_id=company_id, date_planned__year=current_datetime.year,
    #                                                       date_planned__month=current_datetime.month, date_planned__day=current_datetime.day,
    #                                                       status=Order.COMPLETED).annotate(sum_orders=Sum('price')).count()

    #     in_progress_orders = Order.objects.filter(company_id=company_id, date_planned__year=current_datetime.year,
    #                                               date_planned__month=current_datetime.month, date_planned__day=current_datetime.day,
    #                                               status=Order.INPROGRESS)

    #     return Response({'all_today_orders': all_today_orders,
    #                      'all_today_completed_orders': all_today_completed_orders,
    #                      'in_progress_orders': in_progress_orders})
