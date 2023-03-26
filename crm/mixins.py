

class SuperUserAdminMixin:

    def remove_fields(self,request, fields, fields_to_remove=('company',)):
        if request.user.is_superuser:
            return fields 
        for field in fields_to_remove:
            if field in fields: fields.remove(field)
        return fields
    
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(company=request.user.profile.company)

    def get_list_display(self, request):
        list_display = list(super().get_list_display(request))    
        return self.remove_fields(request, list_display)

    def get_fields(self, request, obj=None):
        fields = list(super().get_fields(request, obj))
        return self.remove_fields(request, fields)
    
    def save_model(self, request, obj, form, change):
        if request.user.is_superuser:
            return super().save_model(request, obj, form, change)
        if not obj.id: obj.company = request.user.profile.company
        return super().save_model(request, obj, form, change)

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

class SuperUserInlineAdminMixin:

    def get_fields(self, request, obj=None):
        fields = super().get_fields(request, obj)
        if request.user.is_superuser:
            return fields
        fields_to_remove = ('company', )
        for field in fields_to_remove:
            fields.remove(field)
        return fields