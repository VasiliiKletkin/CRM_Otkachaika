from clients.forms import ClientInlineForm
from clients.models import Client
from companies.mixins import CompanyInlineAdminMixin
from django.contrib import admin
from django_currentuser.middleware import get_current_user

from .forms import AddressForm, CityForm, CountyForm, RegionForm, StreetForm
from .models import Address, City, Country, Region, Street


class CountyAdmin(admin.ModelAdmin):
    form = CountyForm


class RegionAdmin(admin.ModelAdmin):
    form = RegionForm


class CityAdmin(admin.ModelAdmin):
    form = CityForm


class StreetAdmin(admin.ModelAdmin):
    form = StreetForm


class ClientInline(CompanyInlineAdminMixin, admin.StackedInline):
    model = Client
    extra = 1
    form = ClientInlineForm


class AddressAdmin(admin.ModelAdmin):
    search_fields = ("street__name", "home")
    inlines = [
        ClientInline,
    ]
    form = AddressForm

    def get_queryset(self, request):
        user = get_current_user()
        queryset = super().get_queryset(request)
        if not user.is_superuser:
            return queryset.filter(
                street__city__in=user.profile.company.work_place.cities.all()
            )
        return queryset


admin.site.register(Street, StreetAdmin)
admin.site.register(Country, CountyAdmin)
admin.site.register(Region, RegionAdmin)
admin.site.register(City, CityAdmin)
admin.site.register(Address, AddressAdmin)
