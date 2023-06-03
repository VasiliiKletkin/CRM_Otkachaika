from companies.mixins import CompanyAdminMixin
from django.contrib import admin

from .forms import ReportForm
from .models import Report


class ReportAdmin(CompanyAdminMixin, admin.ModelAdmin):
    list_display = (
        "date_start",
        "date_end",
        "date_created",
        "profit",
        "company",
    )
    # list_filter = ('company__name',)
    date_hierarchy = "date_created"
    ordering = ("date_created",)
    form = ReportForm

    def add_view(self, request, extra_content=None):
        self.fields = ("company", "date_start", "date_end")
        self.readonly_fields = ()
        return super().add_view(request)

    def change_view(self, request, object_id, extra_context=None):
        self.fields = (
            "company",
            "date_start",
            "date_end",
            "profit",
            "count_orders",
            "count_new_addresses",
            "count_new_clients",
        )
        self.readonly_fields = (
            "company",
            "date_start",
            "date_end",
            "profit",
            "count_orders",
            "count_new_addresses",
            "count_new_clients",
        )
        return super().change_view(request, object_id, extra_context)


admin.site.register(Report, ReportAdmin)
