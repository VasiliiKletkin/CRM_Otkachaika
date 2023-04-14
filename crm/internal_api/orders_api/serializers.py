from internal_api.addresses_api.serializers import AddressSerializer
from internal_api.companies_api.serializers import CompanySerializer
from internal_api.employees_api.serializers import (DispatcherSerializer,
                                                    DriverSerializer)
from orders.models import Order
from rest_framework import serializers


class OrderSerializer(serializers.ModelSerializer):
    type_payment_display = serializers.CharField(
        source="get_type_payment_display")

    address = AddressSerializer()
    driver = DriverSerializer()
    dispatcher = DispatcherSerializer()

    class Meta:
        model = Order
        fields = '__all__'
