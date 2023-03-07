from dal import autocomplete
from django.db.models import Q
from django_filters.rest_framework import DjangoFilterBackend
from employees.models import Driver
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response
from users.models import Profile, Telegram

from .serializers import DriverSerializer


class DriverViewSet(viewsets.ModelViewSet):
    queryset = Driver.objects.all()
    serializer_class = DriverSerializer

class TelegramViewSet(viewsets.ModelViewSet):
    queryset = Telegram.objects.all()
    serializer_class = DriverSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['telegram_id',]
    
class DriverAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = Driver.objects.filter(profile__user_type=Profile.DRIVER)
        if not self.request.user.is_superuser:
            qs = qs.filter(profile__company=self.request.user.profile.company)
        if self.q:
            qs = qs.filter(Q(first_name__istartswith=self.q)
                           | Q(last_name__istartswith=self.q))
        return qs
