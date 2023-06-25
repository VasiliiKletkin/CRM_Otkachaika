from companies.mixins import CompanyAdminMixin
from django.contrib import admin, messages
from django.contrib.admin import SimpleListFilter
from employees.models import Driver
from orders.forms import OrderForm
from users.models import Profile

from .models import Order


class DriversFilter(SimpleListFilter):
    title = "Водители"
    parameter_name = "driver"

    def lookups(self, request, model_admin):
        qs = Driver.objects.all()
        if not request.user.is_superuser:
            qs = qs.filter(profile__company=request.user.profile.company)
        qs = qs.filter(profile__user_type=Profile.DRIVER)
        return [(driver.id, driver) for driver in qs]

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(driver_id=self.value())


class OrderAdmin(CompanyAdminMixin, admin.ModelAdmin):
    list_filter = ("status", DriversFilter)
    search_fields = (
        "address__street__name",
        "address__home",
        "price",
        "client__first_name",
        "client__last_name",
        "client__phone_number",
    )
    ordering = ("date_created", "date_completed")
    form = OrderForm

    actions = ("uppercase",)

    @admin.action(description="Отправить водителю")
    def uppercase(modeladmin, request, queryset):
        for obj in queryset:
            obj.send_to_driver()
        messages.success(request, "Выбранные заказы были отправлены")

    list_display = (
        "address",
        "price",
        "driver",
        "client",
        "status",
        "company",
    )

    def add_view(self, request, extra_content=None):
        self.fields = (
            "company",
            "driver",
            "address",
            "client",
            "description",
            "price",
            "type_payment",
            "date_planned",
        )
        self.readonly_fields = ()
        return super().add_view(request)

    def change_view(self, request, object_id, extra_context=None):
        self.fields = (
            "company",
            "status",
            "created_by",
            "driver",
            "address",
            "client",
            "description",
            "price",
            "type_payment",
            "date_created",
            "date_planned",
            "date_started",
            "date_completed",
            "is_sent",
        )
        self.readonly_fields = (
            "company",
            "created_by",
            "driver",
            "address",
            "date_created",
            "client",
            "description",
            "date_started",
            "price",
            "type_payment",
            "date_planned",
            "date_completed",
            "is_sent",
        )
        return super().change_view(request, object_id)

    def save_model(self, request, obj, form, change):
        if not change:
            obj.created_by = request.user
        return super().save_model(request, obj, form, change)


admin.site.register(Order, OrderAdmin)
