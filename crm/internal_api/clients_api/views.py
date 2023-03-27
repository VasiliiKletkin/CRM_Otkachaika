from clients.models import Address, City, Street
from dal import autocomplete
from django.db.models import Q


class AddressAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = Address.objects.all()
        if not self.request.user.is_superuser:
            qs = qs.filter(clients__company=self.request.user.profile.company)
        if self.q:
            qs = qs.filter(Q(street__istartswith=self.q)
                           | Q(home__istartswith=self.q))
        return qs


class CitiesAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = City.objects.all()
        if self.q:
            qs = qs.filter(Q(name__istartswith=self.q)
                           | Q(region__name__istartswith=self.q))
        return qs


class StreetAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = Street.objects.all()
        if self.q:
            qs = qs.filter(Q(name__istartswith=self.q))
        return qs
