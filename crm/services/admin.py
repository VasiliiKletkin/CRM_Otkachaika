from django.contrib import admin
from .models import SubscriptionCompany, ServiceProduct


class SubscriptionCompanyAdmin(admin.ModelAdmin):
    list_display = ('company', 'service', 'subscribed_on', 'expiring_on', 'is_active',)
    readonly_fields = ('subscribed_on', 'expiring_on',)


class ServiceProductCompanyAdmin(admin.ModelAdmin):
    list_display = ('title', 'period', 'price',)


admin.site.register(SubscriptionCompany, SubscriptionCompanyAdmin)
admin.site.register(ServiceProduct, ServiceProductCompanyAdmin)
