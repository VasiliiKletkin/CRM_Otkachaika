from django_currentuser.middleware import get_current_user


class CompanyMixin:
    def save(self, *args, **kwargs):
        user = get_current_user()
        if not user.is_superuser and not self.id:
            self.company = user.profile.company
        return super().save(*args, **kwargs)


class CompanyAdminMixin:
    def remove_fields(self, request, fields, fields_to_remove=("company",)):
        user = get_current_user()
        if not user.is_superuser:
            for field in fields_to_remove:
                if field in fields:
                    fields.remove(field)
        return fields

    def get_queryset(self, request):
        user = get_current_user()
        queryset = super().get_queryset(request)
        if not user.is_superuser:
            return queryset.filter(company=user.profile.company)
        return queryset

    def get_list_display(self, request):
        list_display = list(super().get_list_display(request))
        return self.remove_fields(request, list_display)

    def get_fields(self, request, obj=None):
        fields = list(super().get_fields(request, obj))
        return self.remove_fields(request, fields)


class CompanyInlineAdminMixin:
    def remove_fields(self, request, fields, fields_to_remove=("company",)):
        user = get_current_user()
        if not user.is_superuser:
            for field in fields_to_remove:
                if field in fields:
                    fields.remove(field)
        return fields

    def get_fields(self, request, obj=None):
        fields = list(super().get_fields(request, obj))
        return self.remove_fields(request, fields)
