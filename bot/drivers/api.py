import requests

import os
from dotenv import load_dotenv

load_dotenv()


BASE_URL= os.getenv('BASE_URL')

def check_user(telegram_id):
    url = f"{BASE_URL}internal_api/driver/?telegram_id={telegram_id}"
    response = requests.get(url).json()
    return response

def get_orders(driver_id):
    url = f"{BASE_URL}internal_api/orders/today/?driver_id={driver_id}"
    response = requests.get(url).json()
    return response

def completed_order(order_id):
    url = f"{BASE_URL}internal_api/orders/{order_id}/completed/"
    response = requests.get(url).json()
    return response

def started_order(order_id):
    url = f"{BASE_URL}internal_api/orders/{order_id}/started/"
    response = requests.get(url).json()
    return response

def canceled_order(order_id):
    url = f"{BASE_URL}internal_api/orders/{order_id}/canceled/"
    response = requests.get(url).json()
    return response