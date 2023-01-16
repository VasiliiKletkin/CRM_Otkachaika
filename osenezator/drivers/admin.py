from django.contrib import admin

from .models import Driver
from .models import Car 
class DriverAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'phone_number', 'car', 'is_active', 'company')
    list_filter = ('first_name', 'car', 'is_active')
    search_fields = ('first_name', 'last_name', 'phone_number')
    ordering = ('first_name', 'last_name', 'is_active', 'company')

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(company=request.user.profile.company)

    def render_change_form(self, request, context, *args, **kwargs):
        if request.user.is_superuser:
            return super().render_change_form(request, context, *args, **kwargs)
        context['adminform'].form.fields['car'].queryset = Car.objects.filter(company=request.user.profile.company)
        return super().render_change_form(request, context, *args, **kwargs)

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

admin.site.register(Driver, DriverAdmin)

class CarAdmin(admin.ModelAdmin):
    list_display = ('name', 'number', 'company')
    list_filter = ('name',)
    search_fields = ('name', 'number')
    ordering = ('name', 'number', 'company')

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

admin.site.register(Car, CarAdmin)
