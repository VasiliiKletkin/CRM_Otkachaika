from typing import Any, Dict

from companies.mixins import CompanyAdminMixin, CompanyInlineAdminMixin
from django.contrib import admin
from django.contrib.admin.options import InlineModelAdmin
from django.contrib.auth.admin import UserAdmin
from django.forms import BaseInlineFormSet
from django.http.request import HttpRequest
from phonenumber_field.modelfields import PhoneNumberField
from users.admin import ProfileInlineAdmin
from users.models import Profile

from .forms import CarForm, CarInlineForm
from .mixins import EmployeeAminMixin
from .models import Car, Dispatcher, Driver, Owner


class CarAdmin(CompanyAdminMixin, admin.ModelAdmin):
    list_display = (
        "name",
        "number",
        "company",
    )
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


class ProfileEmployeeInlineAdmin(ProfileInlineAdmin):
    def get_fields(self, request, obj=None):
        fields = super().get_fields(request, obj)
        fields_to_remove = ("user_type",)
        for field in fields_to_remove:
            if field in fields:
                fields.remove(field)
        return fields


class CarInlineAdmin(CompanyInlineAdminMixin, admin.StackedInline):
    form = CarInlineForm
    model = Car


class EmployeeAdminMixin(EmployeeAminMixin, UserAdmin):
    inlines = [
        ProfileEmployeeInlineAdmin,
    ]


class DriverAdmin(EmployeeAdminMixin):
    user_type = Profile.DRIVER


class DispatcherAdmin(EmployeeAdminMixin):
    user_type = Profile.DISPATCHER


class OwnerAdmin(EmployeeAdminMixin):
    user_type = Profile.OWNER


admin.site.register(Car, CarAdmin)
admin.site.register(Driver, DriverAdmin)
admin.site.register(Dispatcher, DispatcherAdmin)
admin.site.register(Owner, OwnerAdmin)
