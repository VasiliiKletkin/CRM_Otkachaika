from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from mixins import AdminSuperUserInlineMixin, AdminSuperUserMixin
from users.admin import ProfileInline
from users.models import Profile

from .models import Car, Dispatcher, Driver, Owner


class ProfileInline(ProfileInline):
    model = Profile

    def get_fields(self, request, obj=None):
        fields = super().get_fields(request, obj)
        fields_to_remove = ('user_type', )
        for field in fields_to_remove:
            fields.remove(field)
        return fields


class CarInline(AdminSuperUserInlineMixin, admin.StackedInline):
    model = Car


class DriverAdmin(UserAdmin):
    list_display = ('username', 'first_name', 'last_name', 'is_active', )
    list_filter = ('first_name', 'is_active',)
    search_fields = ('first_name', 'last_name', 'phone_number',)
    ordering = ('first_name', 'last_name', 'is_active',)
    inlines = [ProfileInline, CarInline,]

    def get_queryset(self, request):
        qs = super().get_queryset(request).filter(profile__user_type=Profile.DRIVER)
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


class CarAdmin(AdminSuperUserMixin, admin.ModelAdmin):
    list_display = ('name', 'number', 'company')
    list_filter = ('name',)
    search_fields = ('name', 'number',)
    ordering = ('name', 'number',)

    def render_change_form(self, request, context, *args, **kwargs):
        qs = Driver.objects.filter(profile__user_type=Profile.DRIVER)
        if not request.user.is_superuser:
            qs.filter(profile__company=request.user.profile.company)
        context['adminform'].form.fields['driver'].queryset = qs
        return super().render_change_form(request, context, *args, **kwargs)


class DispatcherAdmin(UserAdmin):
    list_display = ('username', 'first_name', 'last_name', 'is_active', )
    list_filter = ('first_name', 'is_active',)
    search_fields = ('first_name', 'last_name', 'phone_number',)
    ordering = ('first_name', 'last_name', 'is_active',)
    inlines = [ProfileInline,]

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


class OwnerAdmin(UserAdmin):
    list_display = ('username', 'first_name', 'last_name', 'is_active', )
    list_filter = ('first_name', 'is_active',)
    search_fields = ('first_name', 'last_name', 'phone_number',)
    ordering = ('first_name', 'last_name', 'is_active',)
    inlines = [ProfileInline,]

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


admin.site.register(Driver, DriverAdmin)
admin.site.register(Car, CarAdmin)
admin.site.register(Dispatcher, DispatcherAdmin)
admin.site.register(Owner, OwnerAdmin)
