from clients.forms import ClientInlineForm
from clients.models import Client
from django.contrib import admin
from mixins import SuperUserInlineAdminMixin

from .forms import (AddressForm, CityForm, CountyForm, DistrictForm,
                    RegionForm, StreetForm)
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


class ClientInline(SuperUserInlineAdminMixin, admin.StackedInline):
    model = Client
    extra = 1
    form = ClientInlineForm


class AddressAdmin(admin.ModelAdmin):
    search_fields = ('street', 'home')
    inlines = [ClientInline,]
    form = AddressForm

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if not request.user.is_superuser:
            return qs.filter(street__in=request.user.profile.company.work_place.streets.all())
        return qs

    def save_formset(self, request, form, formset, change):
        instances = formset.save(commit=False)
        is_superuser = request.user.is_superuser
        for instance in instances:
            if not is_superuser:
                instance.company = request.user.profile.company
            instance.save()
        return formset.save_m2m()
        

admin.site.register(Street, StreetAdmin)
admin.site.register(District, DistrictAdmin)
admin.site.register(Country, CountyAdmin)
admin.site.register(Region, RegionAdmin)
admin.site.register(City, CityAdmin)
admin.site.register(Address, AddressAdmin)
