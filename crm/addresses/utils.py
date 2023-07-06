from dadata import Dadata
from django.conf import settings

from .models import Address

dadata = Dadata(settings.DADATA_API_TOKEN, settings.DADATA_SECRET_KEY)


def is_address(address_dict):
    return bool(
        address_dict["street_with_type"]
        and address_dict["street_fias_id"]
        and address_dict["house_type"]
        and address_dict["house"]
    )


def get_address_uid(address_dict):
    return f'{address_dict["street_fias_id"]}{address_dict["house"]}'


def get_address_title(address_dict):
    substring = f'{address_dict["house_type"]} {address_dict["house"]}'
    return address_dict["result"].split(substring)[0] + substring


def get_address(address_str):
    address_dict = dadata.clean("address", address_str)
    if not is_address(address_dict):
        raise Exception
    return Address.objects.get(
        uid=get_address_uid(address_dict),
    )


def get_or_create_address(address_str):
    address_dict = dadata.clean("address", address_str)
    if not is_address(address_dict):
        raise Exception
    address, created = Address.objects.get_or_create(
        title=get_address_title(address_dict),
        uid=get_address_uid(address_dict),
        
        country=address_dict['country'],
        country_iso_code=address_dict['country_iso_code'],
    
        region_fias_id=address_dict['region_fias_id'],
        region_with_type=address_dict['region_with_type'],
        region_type=address_dict['region_type'],
        region_type_full=address_dict['region_type_full'],
        region=address_dict['region'],

        city_fias_id=address_dict['city_fias_id'],
        city_with_type=address_dict['city_with_type'],
        city_type=address_dict['city_type'],
        city_type_full=address_dict['city_type_full'],
        city=address_dict['city'],
        
        street_fias_id=address_dict['street_fias_id'],
        street_with_type=address_dict['street_with_type'],
        street_type=address_dict['street_type'],
        street_type_full=address_dict['street_type_full'],
        street=address_dict['street'],
        
    )
    return address
