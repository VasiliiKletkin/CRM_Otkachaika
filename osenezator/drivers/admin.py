from django.contrib import admin

from .models import Driver
from .models import Car 
class DriverAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'phone_number', 'car')
    list_filter = ('first_name', 'car')
    search_fields = ('first_name', 'last_name')
    ordering = ['first_name', 'last_name']

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(company=request.user.profile.company)

admin.site.register(Driver, DriverAdmin)

class CarAdmin(admin.ModelAdmin):
    list_display = ('name', 'number')
    list_filter = ('name', 'number')
    search_fields = ('name', 'number')
    ordering = ['name', 'number']

admin.site.register(Car, CarAdmin)
