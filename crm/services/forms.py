from dal import autocomplete

from .models import CompanyServiceAggregation, CompanyServiceCRM


class ServiceSelect2GenericForeignKeyModelField(autocomplete.Select2GenericForeignKeyModelField):

    def __init__(self, *args, **kwargs):
        kwargs['widget'] = autocomplete.QuerySetSequenceSelect2
        kwargs['model_choice'] = [(CompanyServiceAggregation,), (CompanyServiceCRM,)]
        super().__init__(*args, **kwargs)
