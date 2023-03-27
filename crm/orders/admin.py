from django.contrib import admin
from mixins import SuperUserAdminMixin
from orders.forms import OrderForm

from .models import Order, OrderRequest


class OrderAdmin(SuperUserAdminMixin, admin.ModelAdmin):
    list_display = ('address', 'price', 'driver',
                    'status', 'date_completed', 'company')
    list_filter = ('status', 'driver', 'company__name')
    search_fields = ('address',)
    ordering = ('date_created', 'date_completed')
    form = OrderForm

    def save_model(self, request, obj, form, change):
        if not obj.id:
            obj.dispatcher = request.user
        return super().save_model(request, obj, form, change)

    def add_view(self, request, extra_content=None):
        self.fields = ('company', ('driver', 'address'),
                       'description',  ('price', 'type_payment'), 'date_planned')
        self.fields = ('company', 'driver', 'address', 'description', 'price',
                       'type_payment', 'date_planned')

        self.readonly_fields = ()
        return super().add_view(request)

    def change_view(self, request, object_id, extra_context=None):
        self.fields = ('company', ('status', 'dispatcher'), ('driver', 'address'), 'description',
                       ('price', 'type_payment'), ('date_planned', 'date_started', 'date_completed'), 'is_sent')
        self.fields = ('company', 'status', 'dispatcher', 'driver', 'address', 'description',  'price',
                       'type_payment', 'date_planned', 'date_started', 'date_completed', 'is_sent')
        self.readonly_fields = (
            'company', 'dispatcher', 'date_started', 'date_completed', 'is_sent')
        return super().change_view(request, object_id, extra_context)


class OrderRequestAdmin(OrderAdmin):
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.filter(dispatcher__is_superuser=True)

    def add_view(self, request, extra_content=None):
        self.fields = (('address'), 'description',
                       ('price', 'type_payment'), 'date_planned')
        self.fields = ('address', 'description',  'price',
                       'type_payment', 'date_planned')
        self.readonly_fields = ()
        return super(OrderAdmin, self).add_view(request)

    def change_view(self, request, object_id, extra_context=None):
        self.fields = ('company', ('address'), 'description',
                       ('price', 'type_payment'), 'date_planned')
        self.fields = ('company', 'address', 'description',
                       'price', 'type_payment', 'date_planned')
        self.readonly_fields = (
            'company', 'address', 'description', 'price', 'type_payment', 'date_planned',)
        return super(OrderAdmin, self).change_view(request, object_id, extra_context)


admin.site.register(Order, OrderAdmin)
admin.site.register(OrderRequest, OrderRequestAdmin)
