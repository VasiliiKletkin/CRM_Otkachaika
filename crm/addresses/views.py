from companies.models import Company
from dal import autocomplete
from django.db.models import Q
from clients.models import Client
from .models import Address
from .utils import dadata


class AddressAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = Address.objects.all()

        if self.q:
            if len(self.q.split()) > 1:
                splitted_line = self.q.split()
                qs = qs.filter(
                    Q(home__icontains=splitted_line[0])
                    & Q(street__name__icontains=splitted_line[1])
                    | Q(street__name__icontains=self.q)
                )
            else:
                qs = qs.filter(
                    Q(home__icontains=self.q) | Q(street__name__icontains=self.q)
                )
        return qs


class DadataAddressListAutocomplete(autocomplete.Select2ListView):
    def autocomplete_results(self, results):
        """Return list of strings that match the autocomplete query."""
        if self.q:
            return [address["value"] for address in dadata.suggest("address", self.q)]
        
    # def get_list(self):
    #     if client := self.forwarded.get("client", None):
    #         client = Client.objects.get(id=client)
    #         print(client)
    #         return ["FFFFF"]
