from django.contrib import admin
from mixins import AdminSuperUserMixin

from .models import Car, Driver


class DriverAdmin(AdminSuperUserMixin, admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'phone_number', 'car', 'is_active', 'company', )
    list_filter = ('first_name', 'car', 'is_active', 'company',)
    search_fields = ('first_name', 'last_name', 'phone_number',)
    ordering = ('first_name', 'last_name', 'is_active',)

    def render_change_form(self, request, context, *args, **kwargs):
        if request.user.is_superuser:
            return super().render_change_form(request, context, *args, **kwargs)
        context['adminform'].form.fields['car'].queryset = Car.objects.filter(company=request.user.profile.company)
        return super().render_change_form(request, context, *args, **kwargs)


class CarAdmin(AdminSuperUserMixin, admin.ModelAdmin):
    list_display = ('name', 'number', 'company')
    list_filter = ('name',)
    search_fields = ('name', 'number',)
    ordering = ('name', 'number',)


admin.site.register(Driver, DriverAdmin)
admin.site.register(Car, CarAdmin)
