from django.utils.translation import gettext_lazy as _


class EmployeeAminMixin:
    prepopulated_fields = {
        "username": (
            "first_name",
            "last_name",
        )
    }
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (_("Personal info"), {"fields": ("first_name", "last_name", "email")}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "groups",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
    list_display = ("username", "first_name", "last_name", "is_active", "date_joined")
    list_filter = ("is_active",)
    search_fields = (
        "first_name",
        "last_name",
        "phone_number",
    )
    ordering = (
        "first_name",
        "last_name",
        "is_active",
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "first_name",
                    "last_name",
                    "username",
                    "email",
                    "password1",
                    "password2",
                ),
            },
        ),
    )

    def get_queryset(self, request):
        queryset = super().get_queryset(request).filter(profile__user_type=self.user_type)
        user = request.user
        if not user.is_superuser:
            return queryset.filter(profile__company=user.profile.company)
        return queryset

    def save_model(self, request, obj, form, change):
        if not obj.id:
            obj.is_staff = True
        return super().save_model(request, obj, form, change)

    def save_formset(self, request, form, formset, change):
        for inline_form in formset.forms:
                inline_form.instance.user_type = self.user_type
                inline_form.instance.company = request.user.profile.company
        return super().save_formset(request, form, formset, change)