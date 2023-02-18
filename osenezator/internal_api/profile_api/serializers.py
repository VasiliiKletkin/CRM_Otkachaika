from internal_api.companies_api.serializers import CompanySerializer
from rest_framework import serializers
from users.models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    company = CompanySerializer()

    class Meta:
        model = Profile
        fields = '__all__'
