class CompanyMixin:
    def save(self, *args, **kwargs):
        if not self.request.user.is_superuser and not self.id:
            self.company = self.request.user.profile.company
        return super().save(*args, **kwargs)

    def get_queryset(self):
        queryset = super().get_queryset()
        if not self.request.user.is_superuser:
            return queryset.filter(company=self.request.user.profile.company)
        return queryset


class CompanyAdminMixin:
    def remove_fields(self, request, fields, fields_to_remove=("company",)):
        if not request.user.is_superuser:
            for field in fields_to_remove:
                if field in fields:
                    fields.remove(field)
        return fields

    def get_list_display(self, request):
        list_display = list(super().get_list_display(request))
        return self.remove_fields(request, list_display)

    def get_fields(self, request, obj=None):
        fields = list(super().get_fields(request, obj))
        return self.remove_fields(request, fields)


class CompanyInlineAdminMixin:
    def remove_fields(self, request, fields, fields_to_remove=("company",)):
        if not request.user.is_superuser:
            for field in fields_to_remove:
                if field in fields:
                    fields.remove(field)
        return fields

    def get_fields(self, request, obj=None):
        fields = list(super().get_fields(request, obj))
        return self.remove_fields(request, fields)
