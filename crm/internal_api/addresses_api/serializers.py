from clients.models import Address
from rest_framework import serializers


class AddressSerializer(serializers.ModelSerializer):
    address_display = serializers.SerializerMethodField()

    def get_address_display(self, obj):
        return str(obj)

    class Meta:
        model = Address
        fields = '__all__'
