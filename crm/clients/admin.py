from django.contrib import admin
from .forms import ClientForm
from mixins import SuperUserAdminMixin, SuperUserInlineAdminMixin

from .models import Client


class ClientAdmin(SuperUserAdminMixin, admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'phone_number',
                    'address', 'is_active', 'company',)
    list_filter = ('is_active', 'company',)
    search_fields = ('first_name', 'last_name', 'address', 'is_active')
    ordering = ('is_active',)
    form = ClientForm


admin.site.register(Client, ClientAdmin)
