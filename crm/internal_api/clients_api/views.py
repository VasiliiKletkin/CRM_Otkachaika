from clients.models import Address
from dal import autocomplete
from django.db.models import Q


class AddressAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = Address.objects.all()
        if not self.request.user.is_superuser:
            qs = qs.filter(company=self.request.user.profile.company)
        if self.q:
            qs = qs.filter(Q(street__istartswith=self.q)
                           | Q(home__istartswith=self.q))
        return qs
