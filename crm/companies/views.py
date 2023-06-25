from dal import autocomplete
from django.db.models import Q
from companies.models import Company


class CompanyAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = Company.objects.all()
        
        if not self.request.user.is_superuser:
            qs = qs.filter(profile__company=self.request.user.profile.company)
        if self.q:
            qs = qs.filter(Q(name__icontains=self.q))
        return qs


# class ServiceCompanyAutocomplete(autocomplete.Select2QuerySetView):
#     def get_queryset(self):
#         qs = ServiceCompany.objects.all()
#         if not self.request.user.is_superuser:
#             qs = qs.filter(profile__company=self.request.user.profile.company)
#         if self.q:
#             qs = qs.filter(Q(name__icontains=self.q))
#         return qs
