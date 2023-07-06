from clients.forms import ClientInlineForm
from clients.models import Client
from companies.mixins import CompanyInlineAdminMixin
from django.contrib import admin

from .forms import AddressForm
from .models import Address


class ClientInline(CompanyInlineAdminMixin, admin.StackedInline):
    model = Client
    extra = 1
    form = ClientInlineForm


class AddressAdmin(admin.ModelAdmin):
    search_fields = (
        "street__name",
        "home",
    )
    inlines = [
        ClientInline,
    ]
    form = AddressForm


admin.site.register(Address, AddressAdmin)
