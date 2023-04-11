from addresses.models import Address, City, Country, Region, Street
from dal import autocomplete
from django.db.models import Q


class CountryAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = Country.objects.all()
        if self.q:
            qs = qs.filter(Q(name__icontains=self.q))
        return qs


class RegionAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = Region.objects.all()

        country = self.forwarded.get('country', None)

        if country:
            qs = qs.filter(Q(country=country))

        if self.q:
            qs = qs.filter(Q(name__icontains=self.q))
        return qs


class CityAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = City.objects.all()

        country = self.forwarded.get('country', None)
        if country:
            qs = qs.filter(Q(region__country=country))

        region = self.forwarded.get('region', None)
        if region:
            qs = qs.filter(Q(region=region))

        if self.q:
            qs = qs.filter(Q(name__icontains=self.q)
                           | Q(region__name__icontains=self.q))
        return qs


class StreetAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = Street.objects.all()

        city = self.forwarded.get('city', None)
        cities = self.forwarded.get('cities', None)
        if city:
            cities = [city]
        if cities:
            qs = qs.filter(city__in=cities)

        if not cities and not self.request.user.is_superuser:
            qs = qs.filter(city__in=self.request.user.profile.company.cities.all())

        if self.q:
            qs = qs.filter(Q(name__icontains=self.q))
        return qs


class AddressAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = Address.objects.all()
        if not self.request.user.is_superuser:
            qs = qs.filter(clients__company=self.request.user.profile.company)
        company = self.forwarded.get('company', None)
        if company:
            qs = qs.filter(clients__company=company)
        if self.q:
            if len(self.q.split()) > 1:
                splitted_line = self.q.split()
                qs = qs.filter(Q(home__icontains=splitted_line[1]) & Q(
                    street__name__icontains=splitted_line[0]))
            else:
                qs = qs.filter(Q(home__icontains=self.q)
                               | Q(street__name__icontains=self.q)
                               | Q(street__city__name__icontains=self.q)
                               | Q(street__city__name__icontains=self.q)
                               )
        return qs