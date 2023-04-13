from internal_api.addresses_api.serializers import AddressSerializer
from internal_api.companies_api.serializers import CompanySerializer
from internal_api.employees_api.serializers import DispatcherSerializer, DriverSerializer
from rest_framework import serializers

from orders.models import Order


class OrderSerializer(serializers.ModelSerializer):
    address = AddressSerializer()
    driver = DriverSerializer()
    dispatcher = DispatcherSerializer()
    company = CompanySerializer()

    class Meta:
        model = Order
        fields = '__all__'
