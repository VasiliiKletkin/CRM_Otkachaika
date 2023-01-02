from django.contrib import admin
from .models import Order

class OrderAdmin(admin.ModelAdmin):
    list_display = ('address', 'driver', 'price', 'date_created', 'status', 'date_complited')
    list_filter = ('status', 'address', 'driver')
    search_fields = ('address', 'status')
    date_hierarchy = 'date_created'
    ordering = ['date_created', 'date_complited']

admin.site.register(Order, OrderAdmin)
