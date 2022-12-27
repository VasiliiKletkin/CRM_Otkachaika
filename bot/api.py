import requests

BASE_URL='http://localhost:8000/api/v1/'

def create_user(telegram_id, username):
    url = f"{BASE_URL/bot}"    