from companies.forms import CompanyForm
from django.contrib import admin

from .forms import CompanyAccountingInlineForm, CompanyWorkPlaceInlineForm
from .models import Company, CompanyAccounting, CompanyWorkPlace


class CompanyWorkPlaceInlineAdmin(admin.StackedInline):
    can_delete = False
    model = CompanyWorkPlace
    form = CompanyWorkPlaceInlineForm


class CompanyAccountingInlineAdmin(admin.StackedInline):
    can_delete = False
    model = CompanyAccounting
    form = CompanyAccountingInlineForm


# class SubscriptionCompanyInlineAdmin(admin.StackedInline):
#     extra = 0
#     model = SubscriptionCompany
#     form = SubscriptionsCompanyForm


class CompanyAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "is_active",
    )
    search_fields = ("name",)
    ordering = ("is_active",)
    form = CompanyForm

    def add_view(self, request, extra_content=None):
        self.inlines = []
        return super().add_view(request)

    def change_view(self, request, object_id, extra_context=None):
        self.inlines = [
            CompanyWorkPlaceInlineAdmin,
            CompanyAccountingInlineAdmin,
            # SubscriptionCompanyInlineAdmin,
        ]
        return super().change_view(request, object_id)


class ServiceCompanyAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "period",
        "price",
    )


admin.site.register(Company, CompanyAdmin)
# admin.site.register(ServiceCompany, ServiceCompanyAdmin)
