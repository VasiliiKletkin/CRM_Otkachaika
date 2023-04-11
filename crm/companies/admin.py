from companies.forms import CompanyForm
from django.contrib import admin

from .forms import SubscriptionsCompanyForm
from .models import Company, ServiceCompany, SubscriptionCompany


class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone_number', 'date_created')
    list_filter = ('date_created', 'cities',)
    search_fields = ('name', 'phone_number', 'date_created')
    ordering = ('name', 'date_created', 'cities',)
    form = CompanyForm


class SubscriptionCompanyAdmin(admin.ModelAdmin):
    list_display = ('company', 'service', 'subscribed_on',
                    'expiring_on', 'is_active',)
    readonly_fields = ('subscribed_on', 'expiring_on',)
    form = SubscriptionsCompanyForm


class ServiceCompanyAdmin(admin.ModelAdmin):
    list_display = ('title', 'period', 'price',)


admin.site.register(Company, CompanyAdmin)
admin.site.register(SubscriptionCompany, SubscriptionCompanyAdmin)
admin.site.register(ServiceCompany, ServiceCompanyAdmin)
