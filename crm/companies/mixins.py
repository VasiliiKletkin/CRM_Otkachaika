class CompanyAdminMixin:
    def remove_fields(self, request, fields, fields_to_remove=("company",)):
        user = request.user
        if not user.is_superuser:
            for field in fields_to_remove:
                if field in fields:
                    fields.remove(field)
        return fields
    
    def save_model(self, request, obj, form, change):
        user = request.user
        if not user.is_superuser and not obj.company_id:
            obj.company = user.profile.company
        return super().save_model(request, obj, form, change)
    
    def get_queryset(self, request):
        user = request.user
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
    
    def get_list_filter(self, request):
        list_filter = list(super().get_list_filter(request))
        return self.remove_fields(request, list_filter)


class CompanyInlineAdminMixin:
    def remove_fields(self, request, fields, fields_to_remove=("company",)):
        user = request.user
        if not user.is_superuser:
            for field in fields_to_remove:
                if field in fields:
                    fields.remove(field)
        return fields

    def get_fields(self, request, obj=None):
        fields = list(super().get_fields(request, obj))
        return self.remove_fields(request, fields)
