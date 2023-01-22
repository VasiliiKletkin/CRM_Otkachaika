from rest_framework import serializers

from addresses.serializers import AddressSerializer
from drivers.serializers import DriverSerializer
from .models import Order


class OrderSerializer(serializers.ModelSerializer):
    address = AddressSerializer()
    driver = DriverSerializer()
    class Meta:
        model = Order
        fields = '__all__'
