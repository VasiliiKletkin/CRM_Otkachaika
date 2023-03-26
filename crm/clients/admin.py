from django.contrib import admin
from mixins import SuperUserAdminMixin, SuperUserInlineAdminMixin

from .models import Address, Client


class ClientInline(SuperUserInlineAdminMixin, admin.StackedInline):
    model = Client
    extra = 1


class ClientAdmin(SuperUserAdminMixin, admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'phone_number',
                    'address', 'is_active', 'company',)
    list_filter = ('is_active', 'company',)
    search_fields = ('first_name', 'last_name', 'address', 'is_active')
    ordering = ('is_active',)


class AddressAdmin(admin.ModelAdmin):
    list_display = ('street', 'home', 'city')
    list_filter = ('city',)
    search_fields = ('street', 'home', 'city')
    inlines = [ClientInline,]

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(clients__company=request.user.profile.company)


admin.site.register(Address, AddressAdmin)
admin.site.register(Client, ClientAdmin)
