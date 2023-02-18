from django_filters.rest_framework import DjangoFilterBackend
from reports.models import Report
from rest_framework import viewsets
from rest_framework.pagination import LimitOffsetPagination

from .serializers import ReportSerializer


class ReportViewSet(viewsets.ModelViewSet):
    queryset = Report.objects.order_by('date_created')[:24]
    serializer_class = ReportSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['company',]
    pagination_class = LimitOffsetPagination

