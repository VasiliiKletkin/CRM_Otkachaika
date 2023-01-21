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


admin.site.register(Order, OrderAdmin)
