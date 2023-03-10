import os

import requests

BASE_URL = os.environ.get('BASE_URL')


def get_profile(telegram_id):
    url = f"{BASE_URL}internal_api/users/profile/?telegram_id={telegram_id}"
    return requests.get(url).json()


def get_orders(driver_id):
    url = f"{BASE_URL}internal_api/orders/today/?driver_id={driver_id}"
    return requests.get(url).json()


def completed_order(order_id):
    url = f"{BASE_URL}internal_api/orders/{order_id}/completed/"
    return requests.get(url).json()


def started_order(order_id):
    url = f"{BASE_URL}internal_api/orders/{order_id}/started/"
    return requests.get(url).json()


def canceled_order(order_id):
    url = f"{BASE_URL}internal_api/orders/{order_id}/canceled/"
    return requests.get(url).json()
