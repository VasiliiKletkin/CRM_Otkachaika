from users.models import Telegram
from .serializers import OrderSerializer
from rest_framework.response import Response
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.decorators import action
from orders.models import Order
from django_filters.rest_framework import DjangoFilterBackend
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from rest_framework import viewsets

from .serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @action(detail=False)
    def telegram(self, request, *args, **kwargs):
        telegram_id = request.GET.get('telegram_id')
        if telegram_id:
            telegram = get_object_or_404(Telegram, telegram_id=telegram_id)
            return Response(telegram.user.profile)

