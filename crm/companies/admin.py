from companies.forms import CompanyForm
from django.contrib import admin

from .models import Company, ServiceProductCompany, SubscriptionCompany


class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone_number', 'date_created')
    list_filter = ('date_created', 'work_of_cities',)
    search_fields = ('name', 'phone_number', 'date_created')
    ordering = ('name', 'date_created', 'work_of_cities',)
    form = CompanyForm


class SubscriptionCompanyAdmin(admin.ModelAdmin):
    list_display = ('company', 'service', 'subscribed_on',
                    'expiring_on', 'is_active',)
    readonly_fields = ('subscribed_on', 'expiring_on',)


class ServiceProductCompanyAdmin(admin.ModelAdmin):
    list_display = ('title', 'period', 'price',)


admin.site.register(Company, CompanyAdmin)
admin.site.register(SubscriptionCompany, SubscriptionCompanyAdmin)
admin.site.register(ServiceProductCompany, ServiceProductCompanyAdmin)
