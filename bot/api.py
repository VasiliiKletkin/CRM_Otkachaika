import requests

import os
from dotenv import load_dotenv

load_dotenv()


BASE_URL= os.getenv('BASE_URL')

def check_user(telegram_id):
    url = f"{BASE_URL}api/v1/driver/?telegram_id={telegram_id}"
    response = requests.get(url).text
    return response

def show_orders(driver_id, status = "INPROGRESS"):
    url = f"{BASE_URL}api/v1/order/?driver={driver_id}&status={status}"
    response = requests.get(url).text
    return response

check_user("1")