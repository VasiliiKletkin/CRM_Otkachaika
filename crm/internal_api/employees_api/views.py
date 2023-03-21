from dal import autocomplete
from django.db.models import Q
from employees.models import Driver
from users.models import Profile


class DriverAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = Driver.objects.filter(profile__user_type=Profile.DRIVER)
        if not self.request.user.is_superuser:
            qs = qs.filter(profile__company=self.request.user.profile.company)
        if self.q:
            qs = qs.filter(Q(first_name__istartswith=self.q)
                           | Q(last_name__istartswith=self.q))
        return qs
