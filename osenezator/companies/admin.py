from django.contrib import admin

from .models import Company


class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name','phone_number', 'city', 'date_created')
    list_filter = ('date_created', 'city',)
    search_fields = ('name','phone_number','date_created')
    ordering = ('name','date_created', 'city',)
    
admin.site.register(Company, CompanyAdmin)