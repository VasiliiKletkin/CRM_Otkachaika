from clients.forms import ClientInlineForm
from clients.models import Client
from companies.mixins import CompanyInlineAdminMixin
from django.contrib import admin

from .forms import (
    AddressForm,
    CityForm,
    CountyForm,
    DistrictForm,
    RegionForm,
    StreetForm,
)
from .models import Address, City, Country, District, Region, Street


class CountyAdmin(admin.ModelAdmin):
    form = CountyForm


class RegionAdmin(admin.ModelAdmin):
    form = RegionForm


class CityAdmin(admin.ModelAdmin):
    form = CityForm


class DistrictAdmin(admin.ModelAdmin):
    form = DistrictForm


class StreetAdmin(admin.ModelAdmin):
    form = StreetForm


class ClientInline(CompanyInlineAdminMixin, admin.StackedInline):
    model = Client
    extra = 1
    form = ClientInlineForm


class AddressAdmin(admin.ModelAdmin):
    search_fields = ("street", "home")
    inlines = [
        ClientInline,
    ]
    form = AddressForm


admin.site.register(Street, StreetAdmin)
admin.site.register(District, DistrictAdmin)
admin.site.register(Country, CountyAdmin)
admin.site.register(Region, RegionAdmin)
admin.site.register(City, CityAdmin)
admin.site.register(Address, AddressAdmin)
