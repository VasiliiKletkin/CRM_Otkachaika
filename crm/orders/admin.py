from django.contrib import admin
from mixins import SuperUserAdminMixin
from orders.forms import OrderForm

from .models import Order


class OrderAdmin(SuperUserAdminMixin, admin.ModelAdmin):
    list_display = ('driver', 'address', 'price', 'date_completed', 'status', 'company',)
    list_filter = ('status', 'driver', 'company__name',)
    search_fields = ('address', 'address',)
    ordering = ('date_created', 'date_completed',)
    readonly_fields = ('dispatcher',)
    form = OrderForm
 
    def save_model(self, request, obj, form, change):
        obj.dispatcher = request.user
        return super().save_model(request, obj, form, change)

    
admin.site.register(Order, OrderAdmin)
