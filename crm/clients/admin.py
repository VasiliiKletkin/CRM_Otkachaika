from django.contrib import admin
from mixins import SuperUserAdminMixin

from .forms import ClientForm
from .models import Client


class ClientAdmin(SuperUserAdminMixin, admin.ModelAdmin):
    list_display = ('phone_number', 'first_name', 'last_name',
                    'address', 'is_active', 'company',)
    list_filter = ('is_active', 'company',)
    search_fields = ('first_name', 'last_name', 'address', 'is_active')
    ordering = ('is_active',)
    form = ClientForm


admin.site.register(Client, ClientAdmin)
