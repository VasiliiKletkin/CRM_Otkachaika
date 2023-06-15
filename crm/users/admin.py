from companies.mixins import CompanyInlineAdminMixin
from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import ProfileInlineForm
from .models import Profile

User = get_user_model()


class ProfileInline(CompanyInlineAdminMixin, admin.StackedInline):
    model = Profile
    form = ProfileInlineForm


class CustomUserAdmin(UserAdmin):
    list_display = ("username", "email", "first_name", "last_name", "profile",)
    inlines = [
        ProfileInline,
    ]


admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
