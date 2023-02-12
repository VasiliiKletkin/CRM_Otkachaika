from django.contrib import admin

from osenezator.mixins import AdminSuperUserMixin

from .models import Report


class ReportAdmin(AdminSuperUserMixin, admin.ModelAdmin):
    pass

admin.site.register(Report, ReportAdmin)
