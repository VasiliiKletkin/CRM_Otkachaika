from companies.models import Company
from dal import autocomplete
from django.db.models import Q

from .models import Address, City, Country, District, Region, Street


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
        
        #for workplace
        countries = self.forwarded.get('countries', None)
        if countries:
            qs = qs.filter(country__in=countries)

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
        
        #for workplace
        regions = self.forwarded.get('regions', None)
        if regions:
            qs = qs.filter(region__in=regions)
        
        if self.q:
            qs = qs.filter(Q(name__icontains=self.q))
        return qs


class DistrictAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = District.objects.all()

        country = self.forwarded.get('country', None)
        if country:
            qs = qs.filter(Q(city__region__country=country))

        region = self.forwarded.get('region', None)
        if region:
            qs = qs.filter(Q(city__region=region))

        city = self.forwarded.get('city', None)
        if city:
            qs = qs.filter(Q(city=city))
        
        #for workplace
        cities = self.forwarded.get('cities', None)
        if cities:
            qs = qs.filter(city__in=cities)

        if self.q:
            qs = qs.filter(Q(name__icontains=self.q))
        return qs


class StreetAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = Street.objects.all()

        country = self.forwarded.get('country', None)
        if country:
            qs = qs.filter(Q(district__city__region__country=country))

        region = self.forwarded.get('region', None)
        if region:
            qs = qs.filter(Q(district__city__region=region))

        city = self.forwarded.get('city', None)
        if city:
            qs = qs.filter(Q(district__city=city))
        
        district = self.forwarded.get('district', None)
        if district:
            qs = qs.filter(Q(district=district))

        #for workplace
        districts = self.forwarded.get('districts', None)
        if districts:
            qs = qs.filter(district__in=districts)

        # #for new address
        # if not self.request.user.is_superuser:
        #     qs = qs.filter(street__in=self.request.user.profile.company.cities.all())

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

        if not self.request.user.is_superuser:
            qs = qs.filter(street__in=self.request.user.profile.company.work_place.streets.all())
        else:
            company = self.forwarded.get('company', None)
            if company:
                company = Company.objects.get(id=company)
                qs = qs.filter(street__in=company.streets.all())

        if self.q:
            if len(self.q.split()) > 1:
                splitted_line = self.q.split()
                qs = qs.filter(Q(home__icontains=splitted_line[1]) & Q(
                    street__name__icontains=splitted_line[0]) 
                    | Q(street__name__icontains=self.q))
            else:
                qs = qs.filter(Q(home__icontains=self.q)
                               | Q(street__name__icontains=self.q)
                               | Q(street__city__name__icontains=self.q)
                               | Q(street__city__name__icontains=self.q)
                               )
        return qs