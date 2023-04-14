from django.contrib import admin
from django.contrib.admin import SimpleListFilter
from employees.models import Driver
from mixins import SuperUserAdminMixin
from orders.forms import OrderForm
from users.models import Profile

from .models import Order


class DriversFilter(SimpleListFilter):
    title = 'Водители'
    parameter_name = 'driver'

    def lookups(self, request, model_admin):
        qs = Driver.objects.all()
        if not request.user.is_superuser:
            qs = qs.filter(profile__company=request.user.profile.company)
        qs = qs.filter(profile__user_type=Profile.DRIVER)
        return [(driver.id, driver) for driver in qs]

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(driver_id=self.value())


class OrderAdmin(SuperUserAdminMixin, admin.ModelAdmin):
    list_display = ('address', 'price', 'driver',
                    'status', 'date_completed', 'company')
    list_filter = ('status', DriversFilter)
    search_fields = ('address',)
    ordering = ('date_created', 'date_completed')
    form = OrderForm

    def save_model(self, request, obj, form, change):
        if not obj.id:
            obj.dispatcher = request.user
        return super().save_model(request, obj, form, change)

    def add_view(self, request, extra_content=None):
        self.fields = ('company', ('driver', 'address'), 'client',
                       'description',  ('price', 'type_payment'), 'date_planned')
        self.fields = ('company', 'driver', 'address', 'client', 'description', 'price',
                       'type_payment', 'date_planned')

        self.readonly_fields = ()
        return super().add_view(request)

    def change_view(self, request, object_id, extra_context=None):
        self.fields = ('company', ('status', 'dispatcher'), ('driver', 'address'), 'client', 'description',
                       ('price', 'type_payment'), ('date_planned', 'date_started', 'date_completed'), 'is_sent')
        self.fields = ('company', 'status', 'dispatcher', 'driver', 'address', 'client', 'description',  'price',
                       'type_payment', 'date_planned', 'date_started', 'date_completed', 'is_sent')
        self.readonly_fields = ('company', 'dispatcher', 'driver', 'address',
                                'client', 'description', 'date_started', 'price', 'type_payment', 'date_planned', 'date_completed', 'is_sent')

        return super().change_view(request, object_id, extra_context)


admin.site.register(Order, OrderAdmin)
