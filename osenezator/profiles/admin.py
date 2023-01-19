from django.contrib import admin
from .models import Profile
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model

user_model = get_user_model()

class UserProfileInline(admin.StackedInline):
    model = Profile


class CustomUserAdmin(UserAdmin):

    inlines = [UserProfileInline,]
    
    def get_queryset(self, request):
        qs = super().get_queryset(request).select_related("profile")
        if request.user.is_superuser:
            return qs
        return qs.filter(profile__company=request.user.profile.company)

    def save_model(self, request, obj, form, change):
        obj.is_staff = True
        return super().save_model(request, obj, form, change)

admin.site.unregister(user_model)
admin.site.register(user_model, CustomUserAdmin)
