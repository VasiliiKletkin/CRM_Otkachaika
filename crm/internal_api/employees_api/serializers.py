from employees.models import Dispatcher, Driver, Owner
from internal_api.users_api.serializers import UserSerializer
from rest_framework import serializers


class DriverSerializer(UserSerializer):
    class Meta(UserSerializer.Meta):
        model = Driver


class DispatcherSerializer(UserSerializer):
    class Meta(UserSerializer.Meta):
        model = Dispatcher


class OwnerSerializer(UserSerializer):
    class Meta(UserSerializer.Meta):
        model = Owner
