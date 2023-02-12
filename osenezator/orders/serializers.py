from rest_framework import serializers

from clients.serializers import AddressSerializer
from employees.serializers import DriverSerializer
from .models import Order


class OrderSerializer(serializers.ModelSerializer):
    address = AddressSerializer()
    driver = DriverSerializer()
    class Meta:
        model = Order
        fields = '__all__'
