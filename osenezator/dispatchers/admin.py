
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from profiles.admin import ProfileInline
from profiles.models import Profile

from .models import Dispatcher


class ProfileDispatcherInline(ProfileInline):
    model = Profile

    def get_fields(self, request, obj=None):
        fields = super().get_fields(request, obj)
        fields_to_remove = ('user_type', )
        for field in fields_to_remove:
            fields.remove(field)
        return fields


class DispatcherAdmin(UserAdmin):
    list_display = ('username', 'first_name', 'last_name', 'is_active', )
    list_filter = ('first_name', 'is_active',)
    search_fields = ('first_name', 'last_name', 'phone_number',)
    ordering = ('first_name', 'last_name', 'is_active',)
    inlines = [ProfileDispatcherInline,]

    def get_queryset(self, request):
        qs = super().get_queryset(request).filter(
            profile__user_type=Profile.DISPATCHER)
        return qs

    def save_formset(self, request, form, formset, change):
        instances = formset.save(commit=False)
        is_superuser = request.user.is_superuser
        for instance in instances:
            user_type = hasattr(instance, 'user_type')
            if user_type:
                instance.user_type = Profile.DRIVER
            if not is_superuser:
                instance.company = request.user.profile.company
            instance.save()
        return formset.save_m2m()



admin.site.register(Dispatcher, DispatcherAdmin)
