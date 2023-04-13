from clients.models import Client
from dal import autocomplete
from django.db.models import Q


class ClientAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = Client.objects.all()

        company = self.forwarded.get('company', None)
        if company:
            qs = qs.filter(company=company)

        address = self.forwarded.get('address', None)
        if address:
            qs = qs.filter(address=address)


        if self.q:
            qs = qs.filter(Q(phone_number__icontains=self.q)
                            | Q(first_name__icontains=self.q)
                            | Q(second_name__icontains=self.q)
                            )
        return qs
