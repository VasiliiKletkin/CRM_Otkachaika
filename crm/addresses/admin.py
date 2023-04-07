from clients.models import Client
from django.contrib import admin
from clients.forms import ClientInlineForm

from mixins import SuperUserInlineAdminMixin

from .forms import AddressForm, CityForm, RegionForm, StreetForm
from .models import Address, City, Country, Region, Street


class CountyAdmin(admin.ModelAdmin):
    pass


class RegionAdmin(admin.ModelAdmin):
    form = RegionForm


class CityAdmin(admin.ModelAdmin):
    form = CityForm


class StreetAdmin(admin.ModelAdmin):
    form = StreetForm


class ClientInline(SuperUserInlineAdminMixin, admin.StackedInline):
    model = Client
    extra = 1
    form = ClientInlineForm


class AddressAdmin(admin.ModelAdmin):
    list_display = ('street', 'home', 'city')
    list_filter = ('city',)
    search_fields = ('street', 'home', 'city')
    inlines = [ClientInline,]
    form = AddressForm

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(clients__company=request.user.profile.company)


admin.site.register(Street, StreetAdmin)
admin.site.register(Country, CountyAdmin)
admin.site.register(Region, RegionAdmin)
admin.site.register(City, CityAdmin)
admin.site.register(Address, AddressAdmin)
