from django.contrib import admin
from .models import Address, Client

class AddressAdmin(admin.ModelAdmin):
    list_display = ('address1', 'address2', 'city', 'volume')
    list_filter = ('volume','city',)
    search_fields = ('address1','address2','city', 'volume')
    ordering = ('volume','city')
    
admin.site.register(Address, AddressAdmin)

class ClientAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'phone_number', 'address', 'is_active', 'company')
    list_filter = ('is_active',)
    search_fields = ('first_name','last_name','address','is_active')
    ordering = ('is_active','company')
    

admin.site.register(Client, ClientAdmin)