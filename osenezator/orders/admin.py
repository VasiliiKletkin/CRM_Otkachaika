from django.contrib import admin
from .models import Order

class OrderAdmin(admin.ModelAdmin):
    list_display = ('address', 'driver', 'price', 'date_created', 'status', 'date_complited', 'company')
    list_filter = ('status', 'address', 'driver')
    search_fields = ('address', 'status')
    date_hierarchy = 'date_created'
    ordering = ('date_created', 'date_complited', 'company')

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(company=request.user.profile.company)

admin.site.register(Order, OrderAdmin)
