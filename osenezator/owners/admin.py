
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from users.admin import ProfileInline
from users.models import Profile

from .models import Owner


class ProfileOwnersInline(ProfileInline):
    model = Profile

    def get_fields(self, request, obj=None):
        fields = super().get_fields(request, obj)
        fields_to_remove = ('user_type', )
        for field in fields_to_remove:
            fields.remove(field)
        return fields


class OwnerAdmin(UserAdmin):
    list_display = ('username', 'first_name', 'last_name', 'is_active', )
    list_filter = ('first_name', 'is_active',)
    search_fields = ('first_name', 'last_name', 'phone_number',)
    ordering = ('first_name', 'last_name', 'is_active',)
    inlines = [ProfileOwnersInline,]

    def get_queryset(self, request):
        qs = super().get_queryset(request).filter(
            profile__user_type=Profile.OWNER)
        return qs

    def save_formset(self, request, form, formset, change):
        instances = formset.save(commit=False)
        is_superuser = request.user.is_superuser
        for instance in instances:
            user_type = hasattr(instance, 'user_type')
            if user_type:
                instance.user_type = Profile.OWNER
            if not is_superuser:
                instance.company = request.user.profile.company
            instance.save()
        return formset.save_m2m()


admin.site.register(Owner, OwnerAdmin)
