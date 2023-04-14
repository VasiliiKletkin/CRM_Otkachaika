from rest_framework import serializers
from clients.models import Address


class AddressSerializer(serializers.ModelSerializer):
    address_dysplay_name = serializers.SerializerMethodField()
    def get_address_dysplay_name(self, obj):
        return str(obj)

    class Meta:
        model = Address
        fields = '__all__'