from typing import Any, Dict
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.admin.options import InlineModelAdmin
from django.http.request import HttpRequest
from companies.mixins import CompanyAdminMixin, CompanyInlineAdminMixin
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from users.admin import ProfileInlineAdmin
from users.models import Profile
from django.forms import BaseInlineFormSet
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


class DriverAdmin(EmployeesAminMixin, UserAdmin):
    user_type = Profile.DRIVER
    inlines = [
        ProfileEmployeeInlineAdmin,
    ]

class DispatcherAdmin(EmployeesAminMixin, UserAdmin):
    user_type = Profile.DISPATCHER
    inlines = [
        ProfileEmployeeInlineAdmin,
    ]


class OwnerAdmin(EmployeesAminMixin, UserAdmin):
    user_type = Profile.OWNER
    inlines = [
        ProfileEmployeeInlineAdmin,
    ]


admin.site.register(Car, CarAdmin)
admin.site.register(Driver, DriverAdmin)
admin.site.register(Dispatcher, DispatcherAdmin)
admin.site.register(Owner, OwnerAdmin)
