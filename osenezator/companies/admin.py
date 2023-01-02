from django.contrib import admin
from .models import Company

class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone')
    list_filter = ('name',)
    search_fields = ('name',)
    ordering = ('name',)

admin.site.register(Company, CompanyAdmin)