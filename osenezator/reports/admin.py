from django.contrib import admin
from mixins import SuperUserAdminMixin

from .models import Report


class ReportAdmin(SuperUserAdminMixin, admin.ModelAdmin):

    list_display = ('date_start', 'date_end', 'date_created', 'profit', 'company',)
    list_filter = ('company__name',)
    search_fields = ('id', 'count_orders', 'new_addresses', 'date')
    date_hierarchy = 'date_created'
    ordering = ('date_created',)

admin.site.register(Report, ReportAdmin)
