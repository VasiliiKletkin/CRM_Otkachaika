from django.contrib import admin
from .models import Profile

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'user_type', 'company')
    list_filter = ('user_type','user_type')
    search_fields = ('user', 'user_type')
    ordering = ('user_type','user_type', 'company')

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(company=request.user.profile.company)

    # def render_change_form(self, request, context, *args, **kwargs):
    #     if request.user.is_superuser:
    #         return super().render_change_form(request, context, *args, **kwargs)
    #     context['adminform'].form.fields['user'].queryset = .objects.filter(company=request.user.profile.company)
    #     return super().render_change_form(request, context, *args, **kwargs)

    def get_fields(self, request, obj=None):
        fields = super().get_fields(request, obj)
        if request.user.is_superuser:
            return fields
        fields_to_remove = ('company', )
        for field in fields_to_remove:
            fields.remove(field)
        return fields

    def save_model(self, request, obj, form, change):
        if request.user.is_superuser:
            super().save_model(request, obj, form, change)
        obj.company = request.user.profile.company
        super().save_model(request, obj, form, change)

admin.site.register(Profile, ProfileAdmin)