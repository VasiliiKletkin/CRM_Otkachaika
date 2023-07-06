from django.contrib import admin
from .models import CompanyServiceAggregation, CompanyServiceCRM



class CompanyServiceAggregationAdmin(admin.ModelAdmin):
    pass

class CompanyServiceCRMAdmin(admin.ModelAdmin):
    pass


admin.site.register(CompanyServiceAggregation, CompanyServiceAggregationAdmin)

admin.site.register(CompanyServiceCRM, CompanyServiceCRMAdmin)
