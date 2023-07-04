from dadata import Dadata
from django.conf import settings
from .models import Address


dadata = Dadata(settings.DADATA_API_TOKEN, settings.DADATA_SECRET_KEY)

def is_address(address_dict):
    return bool(
        address_dict["region_with_type"]
        and address_dict['region_fias_id']
        # and address_dict['city_with_type'] msk and piter dont have city
        and address_dict["street_with_type"]
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
    return Address.objects.get(uid=get_address_uid(address_dict), title=get_address_title(address_dict))

def get_or_create_address(address_str):
    address_dict = dadata.clean("address", address_str)
    if not is_address(address_dict):
        raise Exception
    address, created = Address.objects.get_or_create(uid=get_address_uid(address_dict), title=get_address_title(address_dict))
    return address