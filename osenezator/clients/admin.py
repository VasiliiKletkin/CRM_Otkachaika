from django.contrib import admin
from .models import Address, Client

class AddressAdmin(admin.ModelAdmin):
    list_display = ('address1', 'address2', 'city', 'volume','company')
    list_filter = ('volume','city',)
    search_fields = ('address1','address2','city', 'volume')
    ordering = ('volume', 'city','company')
    
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(company=request.user.profile.company)

    def get_fields(self, request, obj=None):
        fields = super().get_fields(request, obj)
        if request.user.is_superuser:
            return fields
        fields_to_remove = ('company', )
        for field in fields_to_remove:
            fields.remove(field)
        return fields

    def save_model(self, request, obj, form, change):
        if request.user.is_superuser:
            super().save_model(request, obj, form, change)
        obj.company = request.user.profile.company
        super().save_model(request, obj, form, change)

admin.site.register(Address, AddressAdmin)

class ClientAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'phone_number', 'address', 'is_active', 'company')
    list_filter = ('is_active',)
    search_fields = ('first_name','last_name','address','is_active')
    ordering = ('is_active','company')

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(company=request.user.profile.company)

    def get_fields(self, request, obj=None):
        fields = super().get_fields(request, obj)
        if request.user.is_superuser:
            return fields
        fields_to_remove = ('company', )
        for field in fields_to_remove:
            fields.remove(field)
        return fields

    def save_model(self, request, obj, form, change):
        if request.user.is_superuser:
            super().save_model(request, obj, form, change)
        obj.company = request.user.profile.company
        super().save_model(request, obj, form, change)

admin.site.register(Client, ClientAdmin)