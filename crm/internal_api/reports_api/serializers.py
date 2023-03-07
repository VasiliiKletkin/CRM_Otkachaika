from internal_api.companies_api.serializers import CompanySerializer
from rest_framework import serializers

from reports.models import Report


class ReportSerializer(serializers.ModelSerializer):
    company = CompanySerializer()

    class Meta:
        model = Report
        fields = '__all__'
