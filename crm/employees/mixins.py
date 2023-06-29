from django.utils.translation import gettext_lazy as _


class EmployeesAminMixin:
    prepopulated_fields = {
        "username": (
            "first_name",
            "last_name",
        )
    }
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email')}),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'groups',),
        }),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    list_display = (
        "username",
        "first_name",
        "last_name",
        "is_active",
        "date_joined"
    )
    list_filter = (
        "is_active",
    )
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
        user = request.user
        queryset = super().get_queryset(request).filter(profile__user_type=self.user_type)
        if not user.is_superuser:
            return queryset.filter(profile__company=user.profile.company)
        return queryset

    def save_model(self, request, obj, form, change):
        if not obj.id:
            obj.is_staff = True
        return super().save_model(request, obj, form, change)

    def save_formset(self, request, form, formset, change):
        instances = formset.save(commit=False)
        for instance in instances:
            user_type = hasattr(instance, "user_type")
            if user_type:
                instance.user_type = self.user_type
            instance.save()
        return formset.save_m2m()
