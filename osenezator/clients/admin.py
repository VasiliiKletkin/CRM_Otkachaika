from django.contrib import admin
from .models import Address, Client

class AddressAdmin(admin.ModelAdmin):
    list_display = ('address1', 'volume')
    list_filter = ('address1', 'volume')
    search_fields = ('address1',)
    ordering = ('address1',)

admin.site.register(Address, AddressAdmin)

class ClientAdmin(admin.ModelAdmin):
    pass

admin.site.register(Client, ClientAdmin)