from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from mixins import AdminSuperUserInlineMixin

from .models import Profile

user_model = get_user_model()


class ProfileInline(AdminSuperUserInlineMixin, admin.StackedInline):
    model = Profile


class CustomUserAdmin(UserAdmin):
    list_display= ('username', 'email', 'first_name', 'last_name', 'profile')
    inlines = [ProfileInline,]

    def get_queryset(self, request):
        qs = super().get_queryset(request).prefetch_related('profile')
        if request.user.is_superuser:
            return qs
        return qs.filter(profile__company=request.user.profile.company)

    # def save_model(self, request, obj, form, change):
    #     obj.is_staff = True
    #     return super().save_model(request, obj, form, change)

    def save_formset(self, request, form, formset, change):
        instances = formset.save(commit=False)
        if request.user.is_superuser:
            for instance in instances:
                instance.save()
            return formset.save_m2m()

        for instance in instances:
            instance.company = request.user.profile.company
            instance.save()
        return formset.save_m2m()


admin.site.unregister(user_model)
admin.site.register(user_model, CustomUserAdmin)
