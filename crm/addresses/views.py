from companies.models import Company
from dal import autocomplete
from django.db.models import Q

from .models import Address, City, Country, Region, Street


class CountryAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = Country.objects.all()
        if self.q:
            qs = qs.filter(Q(name__icontains=self.q))
        return qs


class RegionAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = Region.objects.all()

        if country := self.forwarded.get('country', None):
            qs = qs.filter(Q(country=country))

        if countries := self.forwarded.get('countries', None):
            qs = qs.filter(country__in=countries)

        if self.q:
            qs = qs.filter(Q(name__icontains=self.q))
        return qs


class CityAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = City.objects.all()

        if country := self.forwarded.get('country', None):
            qs = qs.filter(Q(region__country=country))

        if region := self.forwarded.get('region', None):
            qs = qs.filter(Q(region=region))

        if regions := self.forwarded.get('regions', None):
            qs = qs.filter(region__in=regions)

        if self.q:
            qs = qs.filter(Q(name__icontains=self.q))
        return qs


class StreetAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = Street.objects.all()

        if country := self.forwarded.get('country', None):
            qs = qs.filter(Q(city__region__country=country))

        if region := self.forwarded.get('region', None):
            qs = qs.filter(Q(city__region=region))

        if city := self.forwarded.get('city', None):
            qs = qs.filter(Q(city=city))

        if cities := self.forwarded.get('cities', None):
            qs = qs.filter(city__in=cities)

        #for new addresses from owner
        # if not cities and not self.request.user.is_superuser:
        #     qs = self.request.user.profile.company.work_place.streets.all()

        if self.q:
            if len(self.q.split()) > 1:
                splitted_line = self.q.split()
                qs = qs.filter(Q(name__icontains=splitted_line[1]) & Q(name__icontains=splitted_line[0]))
            else:
                qs = qs.filter(Q(name__icontains=self.q))
        return qs


class AddressAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = Address.objects.all()
        # if not self.request.user.is_superuser:
        #     qs = qs.filter(street__in=self.request.user.profile.company.work_place.regions.all())
        # elif company := self.forwarded.get('company', None):
        #     company = Company.objects.get(id=company)
        #     qs = qs.filter(street__in=company.work_place.streets.all())
        if self.q:
            if len(self.q.split()) > 1:
                splitted_line = self.q.split()
                qs = qs.filter(Q(home__icontains=splitted_line[1]) & Q(
                    street__name__icontains=splitted_line[0]) 
                    | Q(street__name__icontains=self.q))
            else:
                qs = qs.filter(Q(home__icontains=self.q) | Q(street__name__icontains=self.q))
        return qs