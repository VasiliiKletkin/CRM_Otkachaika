from companies.mixins import CompanyAdminMixin
from django.contrib import admin

from .forms import ClientForm
from .models import Client


class ClientAdmin(CompanyAdminMixin, admin.ModelAdmin):
    list_display = (
        "phone_number",
        "first_name",
        "last_name",
        "address",
        "is_active",
        "company",
        "date_created",
    )
    list_filter = (
        "is_active",
        "company",
    )
    fields = (
        "phone_number",
        "first_name",
        "last_name",
        "address",
        "is_active",
        "company",
        "date_created",
    )
    readonly_fields = (
        "company",
        "date_created",
    )
    search_fields = ("phone_number", "first_name", "last_name", "address__home", "address__street__name",)
    ordering = ("is_active",)
    form = ClientForm


admin.site.register(Client, ClientAdmin)
