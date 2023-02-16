from clients.serializers import AddressSerializer
from companies.serializers import CompanySerializer
from employees.serializers import DispatcherSerializer, DriverSerializer
from rest_framework import serializers

from .models import Order


class OrderSerializer(serializers.ModelSerializer):
    address = AddressSerializer()
    driver = DriverSerializer()
    dispatcher = DispatcherSerializer()
    company = CompanySerializer()

    class Meta:
        model = Order
        fields = '__all__'
