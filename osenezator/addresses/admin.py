from clients.admin import ClientInline
from django.contrib import admin
from mixins import AdminSuperUserMixin

from .models import Address


class AddressAdmin(AdminSuperUserMixin, admin.ModelAdmin):
    list_display = ('street', 'home', 'city', 'company',)
    list_filter = ('city', 'company',)
    search_fields = ('street', 'home', 'city',)
    inlines = [ClientInline,]
    

admin.site.register(Address, AddressAdmin)
