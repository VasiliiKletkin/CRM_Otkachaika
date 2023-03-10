from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response
from users.models import Profile

from .serializers import ProfileSerializer, UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    pagination_class = LimitOffsetPagination

    @action(detail=True)
    def profile(self, request, pk=None):
        user = get_object_or_404(User, pk=pk)
        serializer = ProfileSerializer(user.profile)
        return Response(serializer.data)

    @action(detail=False)
    def profile(self, request, *args, **kwargs):
        telegram_id = request.GET.get('telegram_id')
        if telegram_id:
            profile = get_object_or_404(Profile, telegram_id=telegram_id)
            serializer = ProfileSerializer(profile)
            return Response(serializer.data)
