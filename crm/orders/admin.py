from django.contrib import admin
from mixins import SuperUserAdminMixin
from orders.forms import OrderForm

from .models import Order


class OrderAdmin(SuperUserAdminMixin, admin.ModelAdmin):
    list_display = ('driver', 'address', 'price', 'date_completed', 'status', 'company',)
    list_filter = ('status', 'driver', 'company__name',)
    search_fields = ('address', 'address',)
    ordering = ('date_created', 'date_completed',)
    form = OrderForm

    def save_model(self, request, obj, form, change):
        obj.dispatcher = request.user
        return super().save_model(request, obj, form, change)

    def add_view(self, request, extra_content=None):
        self.fields = (('driver','address'), 'description',  ('price', 'type_payment'), 'date_planned')
        self.exclude = ('status', 'dispatcher', 'date_started', 'date_completed', 'is_showed')
        return super().add_view(request)
    
    def change_view(self, request, object_id, extra_context=None):
        # self.fields = (('status', 'dispatcher'), ('driver','address'), 'description',  ('price', 'type_payment'), ('date_planned', 'date_started', 'date_completed'), 'is_showed')
        self.readonly_fields = ('dispatcher', 'date_planned', 'date_started', 'date_completed', 'is_showed')
        return super().change_view(request, object_id, extra_context)

admin.site.register(Order, OrderAdmin)