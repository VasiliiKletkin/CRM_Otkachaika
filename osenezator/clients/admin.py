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
    exclude = ['company',]

    def save_model(self, request, obj, form, change):
        if request.user.is_superuser:
            return super().save_model(request, obj, form, change)
        obj.company = request.user.profile.company
        super().save_model(request, obj, form, change)

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(company=request.user.profile.company)

admin.site.register(Client, ClientAdmin)