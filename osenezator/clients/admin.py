from django.contrib import admin
from .models import Address, Client

class AddressAdmin(admin.ModelAdmin):
    list_display = ('address1', 'city', 'volume')
    list_filter = ('volume','city',)
    search_fields = ('address1','city',)
    ordering = ('volume','city',)

admin.site.register(Address, AddressAdmin)

class ClientAdmin(admin.ModelAdmin):
    pass

admin.site.register(Client, ClientAdmin)