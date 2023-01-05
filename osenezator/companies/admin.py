from django.contrib import admin
from .models import Company

class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name','phone_number','date_created')
    list_filter = ('date_created',)
    search_fields = ('name','phone_number','date_created')
    ordering = ('name','date_created')

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(company=request.user.profile.company)

admin.site.register(Company, CompanyAdmin)