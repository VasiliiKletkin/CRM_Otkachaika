class EmployeesAminMixin:
    prepopulated_fields = {
        "username": (
            "first_name",
            "last_name",
        )
    }
    list_display = (
        "username",
        "first_name",
        "last_name",
        "is_active",
    )
    list_filter = (
        "first_name",
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
        return super().get_queryset(request).filter(profile__user_type=self.user_type)

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
