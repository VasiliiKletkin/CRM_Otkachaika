from django.contrib import admin
from .models import Profile

class ProfileAdmin(admin.ModelAdmin):

    list_display = ('user', 'user_type')
    list_filter = ('user_type',)
    search_fields = ('user','user_type')
    ordering = ('user_type',)

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(company=request.user.profile.company)

admin.site.register(Profile, ProfileAdmin)