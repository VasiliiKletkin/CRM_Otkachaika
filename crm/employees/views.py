from dal import autocomplete
from django.db.models import Q
from employees.models import Car, Driver
from users.models import Profile


class DriverAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = Driver.objects.filter(profile__user_type=Profile.DRIVER)

        if not self.request.user.is_superuser:
            qs = qs.filter(profile__company=self.request.user.profile.company)
        else:
            company = self.forwarded.get('company', None)
            if company:
                qs = qs.filter(profile__company=company)
                
        if self.q:
            qs = qs.filter(Q(first_name__icontains=self.q)
                           | Q(last_name__icontains=self.q))
        return qs


class CarAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = Car.objects.filter(profile__user_type=Profile.DRIVER)
        if not self.request.user.is_superuser:
            qs = qs.filter(profile__company=self.request.user.profile.company)
        company = self.forwarded.get('company', None)
        if company:
            qs = qs.filter(profile__company=company)

        if self.q:
            qs = qs.filter(Q(first_name__icontains=self.q)
                           | Q(last_name__icontains=self.q))
        return qs