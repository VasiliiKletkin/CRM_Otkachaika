from typing import Any
from django.http.request import HttpRequest
from django.http.response import HttpResponse
from companies.mixins import CompanyAdminMixin
from django.contrib import admin
from django.utils.html import format_html
from django.utils.safestring import mark_safe

from .forms import ClientForm
from .models import Client, ClientAnalytics, ClientBilling, ClientStatistics


class ClientStatisticsInlineAdmin(admin.StackedInline):
    model = ClientStatistics
    extra = 1
    readonly_fields = (
        "first_completed_order",
        "last_completed_order",
        "count_completed_orders",
    )


class ClientAnalyticsInlineAdmin(admin.StackedInline):
    model = ClientAnalytics
    extra = 1
    readonly_fields = (
        "average_quantity_days_for_order",
        "date_planned_next_order",
    )


class ClientAdmin(CompanyAdminMixin, admin.ModelAdmin):
    form = ClientForm

    def add_view(self, request, extra_content=None):
        self.inlines = []
        return super().add_view(request)

    def change_view(self, request, object_id, extra_context=None):
        self.inlines = [
            ClientStatisticsInlineAdmin,
            ClientAnalyticsInlineAdmin,
        ]
        return super().change_view(request, object_id)

    list_display = (
        "phone_number",
        "first_name",
        "last_name",
        "address",
        "is_active",
        "company",
    )
    list_filter = (
        "is_active",
        "company",
    )
    fields = (
        "phone_number",
        "first_name",
        "last_name",
        "address",
        "is_active",
        "company",
        "date_created",
    )
    readonly_fields = ("date_created",)
    search_fields = (
        "phone_number",
        "first_name",
        "last_name",
        "address__home",
        "address__street__name",
        "address__street__city__name",
    )
    ordering = ("date_created",)


class ClientBillingAdmin(ClientAdmin):
    list_display = (
        "phone_number",
        "first_name",
        "last_name",
        "address",
        "button_call",
        "get_date_planned_next_order",
        "company",
    )

    list_prefetch_related = ("analytics",)

    def get_queryset(self, request):
        return super().get_queryset(request).filter(is_active=True)

    def get_date_planned_next_order(self, obj):
        return obj.analytics.date_planned_next_order

    get_date_planned_next_order.short_description = "Планируемая дата следующего заказа"
    get_date_planned_next_order.admin_order_field = "analytics__date_planned_next_order"

    def button_call(self, obj):
        result_html = format_html(
            f'<a class="button" href="{obj.get_url_phone_number()}">Позвонить</a>&nbsp;'
        )
        return mark_safe(result_html)

    button_call.short_description = "Звонок"
    
    # This will help you to disbale add functionality
    def has_add_permission(self, request):
        return False

    # This will help you to disable delete functionaliyt
    def has_delete_permission(self, request, obj=None):
        return False


admin.site.register(Client, ClientAdmin)
admin.site.register(ClientBilling, ClientBillingAdmin)
