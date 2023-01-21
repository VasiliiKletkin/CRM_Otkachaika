from dal import autocomplete
from django.db.models import Q
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.pagination import LimitOffsetPagination

from .models import Driver
from .serializers import DriverSerializer


class DriverViewSet(viewsets.ModelViewSet):
    queryset = Driver.objects.all()
    serializer_class = DriverSerializer
    filter_backends = [DjangoFilterBackend]
    #filterset_fields = ['telegram_id',]
    pagination_class = LimitOffsetPagination


class DriverAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = Driver.objects.all()
        if not self.request.user.is_superuser:
            qs = qs.filter(company=self.request.user.profile.company)
        if self.q:
            qs = qs.filter(Q(first_name__istartswith=self.q)
                           | Q(last_name__istartswith=self.q))
        return qs
