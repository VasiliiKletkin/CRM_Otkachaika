from companies.forms import CompanyForm
from django.contrib import admin

from .forms import (AccountingCompanyInlineForm, SubscriptionsCompanyForm,
                    WorkPlaceCompanyInlineForm)
from .models import (AccountingCompany, Company, ServiceCompany,
                     SubscriptionCompany, WorkPlaceCompany)


class WorkPlaceCompanyInlineAdmin(admin.StackedInline):
    model = WorkPlaceCompany
    form = WorkPlaceCompanyInlineForm


class AccountingCompanyInlineAdmin(admin.StackedInline):
    model = AccountingCompany
    form = AccountingCompanyInlineForm


class SubscriptionCompanyInlineAdmin(admin.StackedInline):
    model = SubscriptionCompany
    form = SubscriptionsCompanyForm


class CompanyAdmin(admin.ModelAdmin):
    # list_display = ('name', 'date_created')
    # list_filter = ('date_created', 'cities',)
    # search_fields = ('name', 'phone_number', 'date_created')
    # ordering = ('name', 'date_created', 'cities',)
    form = CompanyForm
    inlines = [
        WorkPlaceCompanyInlineAdmin,
        AccountingCompanyInlineAdmin,
        SubscriptionCompanyInlineAdmin,
    ]


class ServiceCompanyAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "period",
        "price",
    )


admin.site.register(Company, CompanyAdmin)
admin.site.register(ServiceCompany, ServiceCompanyAdmin)
