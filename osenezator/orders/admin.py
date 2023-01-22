from django.contrib import admin
from mixins import AdminSuperUserMixin
from orders.forms import OrderForm

from .models import Order


class OrderAdmin(AdminSuperUserMixin, admin.ModelAdmin):
    list_display = ('driver', 'address', 'price', 'date_created', 'date_complited', 'status', 'company',)
    list_filter = ('status', 'driver', 'company__name',)
    search_fields = ('address', 'address',)
    date_hierarchy = 'date_created'
    ordering = ('date_created', 'date_complited',)
    form = OrderForm

    def get_fields(self, request, obj=None):
        fields = super().get_fields(request, obj)
        if request.user.is_superuser:
            return fields
        fields_to_remove = ('dispatcher', )
        for field in fields_to_remove:
            fields.remove(field)
        return fields
    
    def save_model(self, request, obj, form, change):
        if request.user.is_superuser:
            return super().save_model(request, obj, form, change)
        obj.dispatcher = request.user
        return super().save_model(request, obj, form, change)

    
admin.site.register(Order, OrderAdmin)
