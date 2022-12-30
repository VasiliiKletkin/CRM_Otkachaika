import requests
import json

import os

BASE_URL= os.getenv('BASE_URL')

def check_user(telegram_id):
    url = f"{BASE_URL}/driver?telegram_id_"
    response = requests.get(url).text
    return response
