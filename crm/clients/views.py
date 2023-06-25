from .models import Client
from dal import autocomplete
from django.db.models import Q


class ClientAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = Client.objects.all()
        
        if not self.request.user.is_superuser:
            qs = qs.filter(company=self.request.user.profile.company)
        elif company := self.forwarded.get("company", None):
            qs = qs.filter(company=company)

        if address := self.forwarded.get("address", None):
            qs = qs.filter(address=address)

        if self.q:
            qs = qs.filter(
                Q(phone_number__icontains=self.q)
                | Q(first_name__icontains=self.q)
                | Q(last_name__icontains=self.q)
            )
        return qs
