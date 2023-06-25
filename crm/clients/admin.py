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
        "first_order",
        "last_order",
        "count_completed_orders",
    )


class ClientAnalyticsInlineAdmin(admin.StackedInline):
    model = ClientAnalytics
    extra = 1
    readonly_fields = ("average_date_orders", "date_planned_next_order")


class ClientAdmin(CompanyAdminMixin, admin.ModelAdmin):
    form = ClientForm
    inlines = [
        ClientStatisticsInlineAdmin,
        ClientAnalyticsInlineAdmin,
    ]

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
    )
    ordering = ("date_created",)


class ClientBillingAdmin(ClientAdmin):
    list_display = (
        "phone_number",
        "first_name",
        "last_name",
        "address",
        "is_active",
        "get_date_planned_next_order",
        "button_call",
        "company",
    )
    list_editable = ("is_active",)
    list_prefetch_related = ("client_analytics",)

    def get_queryset(self, request):
        return super().get_queryset(request).filter(is_active=True)

    def get_date_planned_next_order(self, obj):
        return obj.client_analytics.date_planned_next_order

    get_date_planned_next_order.short_description = "Планируемая дата следующего заказа"
    get_date_planned_next_order.admin_order_field = "client_analytics__date_planned_next_order"

    def button_call(self, obj):
        result_html = format_html(
            f'<a class="button" href="{obj.get_url_phone_number()}">Позвонить</a>&nbsp;'
        )
        return mark_safe(result_html)

    button_call.short_description = "Звонок"


admin.site.register(Client, ClientAdmin)
admin.site.register(ClientBilling, ClientBillingAdmin)
