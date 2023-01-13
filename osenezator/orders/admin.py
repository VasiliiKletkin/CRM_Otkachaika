from django.contrib import admin
from .models import Order
from drivers.models import Driver
from clients.models import Client

class OrderAdmin(admin.ModelAdmin):
    list_display = ('driver', 'client', 'price', 'date_created', 'date_complited', 'status', 'company')
    list_filter = ('status', 'client', 'driver')
    search_fields = ('client', 'status')
    date_hierarchy = 'date_created'
    ordering = ('date_created', 'date_complited', 'company')

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(company=request.user.profile.company)

    def render_change_form(self, request, context, *args, **kwargs):
        if request.user.is_superuser:
            return super().render_change_form(request, context, *args, **kwargs)
        context['adminform'].form.fields['driver'].queryset = Driver.objects.filter(company=request.user.profile.company)
        context['adminform'].form.fields['client'].queryset = Client.objects.filter(company=request.user.profile.company)
        return super().render_change_form(request, context, *args, **kwargs)

admin.site.register(Order, OrderAdmin)
