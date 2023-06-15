from companies.mixins import CompanyAdminMixin, CompanyInlineAdminMixin
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from users.admin import ProfileInline
from users.models import Profile

from .forms import CarForm, CarInlineForm
from .mixins import EmployeesAminMixin
from .models import Car, Dispatcher, Driver, Owner


class CarAdmin(CompanyAdminMixin, admin.ModelAdmin):
    list_display = ("name", "number", "company")
    list_filter = ("name",)
    search_fields = (
        "name",
        "number",
    )
    ordering = (
        "name",
        "number",
    )
    form = CarForm


class ProfileEmployeeInline(ProfileInline):
    def get_fields(self, request, obj=None):
        fields = super().get_fields(request, obj)
        fields_to_remove = ("user_type",)
        for field in fields_to_remove:
            if field in fields:
                fields.remove(field)
        return fields


class CarInline(CompanyInlineAdminMixin, admin.StackedInline):
    form = CarInlineForm
    model = Car


class DriverAdmin(EmployeesAminMixin, UserAdmin):
    user_type = Profile.DRIVER
    inlines = [
        ProfileEmployeeInline,
        CarInline,
    ]


class DispatcherAdmin(EmployeesAminMixin, UserAdmin):
    user_type = Profile.DISPATCHER
    inlines = [
        ProfileEmployeeInline,
    ]


class OwnerAdmin(EmployeesAminMixin, UserAdmin):
    user_type = Profile.OWNER
    inlines = [
        ProfileEmployeeInline,
    ]


admin.site.register(Car, CarAdmin)
admin.site.register(Driver, DriverAdmin)
admin.site.register(Dispatcher, DispatcherAdmin)
admin.site.register(Owner, OwnerAdmin)
