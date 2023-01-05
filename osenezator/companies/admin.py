from django.contrib import admin
from .models import Company

class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name','phone_number','date_created')
    list_filter = ('date_created',)
    search_fields = ('name','phone_number','date_created')
    ordering = ('name','date_created')
    
admin.site.register(Company, CompanyAdmin)