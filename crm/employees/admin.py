from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from mixins import SuperUserAdminMixin, SuperUserInlineAdminMixin
from users.admin import ProfileInline
from users.forms import ProfileInlineForm
from users.models import Profile

from .models import Car, Dispatcher, Driver, Owner


class CarAdmin(SuperUserAdminMixin, admin.ModelAdmin):
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


class ProfileInline(SuperUserInlineAdminMixin, admin.StackedInline):
    model = Profile
    form = ProfileInlineForm

    def get_fields(self, request, obj=None):
        fields = super().get_fields(request, obj)
        fields_to_remove = ('user_type', )
        for field in fields_to_remove:
            fields.remove(field)
        return fields


class EmployeesAminMixin:
    list_display = ('username', 'first_name', 'last_name', 'is_active', )
    list_filter = ('first_name', 'is_active',)
    search_fields = ('first_name', 'last_name', 'phone_number',)
    ordering = ('first_name', 'last_name', 'is_active',)
    inlines = [ProfileInline,]

    def get_queryset(self, request):
        qs = super().get_queryset(request).filter(profile__user_type=self.user_type)
        return qs

    def save_model(self, request, obj, form, change):
        if not obj.id:
            obj.is_staff = True
        return super().save_model(request, obj, form, change)

    def save_formset(self, request, form, formset, change):
        instances = formset.save(commit=False)
        is_superuser = request.user.is_superuser
        for instance in instances:
            user_type = hasattr(instance, 'user_type')
            if user_type:
                instance.user_type = self.user_type
            if not is_superuser:
                instance.company = request.user.profile.company
            instance.save()
        return formset.save_m2m()


class CarInline(SuperUserInlineAdminMixin, admin.StackedInline):
    model = Car


class DriverAdmin(EmployeesAminMixin, UserAdmin):
    user_type = Profile.DRIVER
    inlines = [ProfileInline, CarInline,]


class DispatcherAdmin(EmployeesAminMixin, UserAdmin):
    user_type = Profile.DISPATCHER


class OwnerAdmin(EmployeesAminMixin, UserAdmin):
    user_type = Profile.OWNER


admin.site.register(Car, CarAdmin)
admin.site.register(Driver, DriverAdmin)
admin.site.register(Dispatcher, DispatcherAdmin)
admin.site.register(Owner, OwnerAdmin)
