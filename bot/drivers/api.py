import os
from aiohttp import web

import aiohttp

BASE_URL = os.environ.get('BASE_URL')

async def error_middleware(session, url):
    try:
        async with session.get(url) as resp:
            if resp.status:
                return await resp.json()
    except Exception as e:
            print({"http error": f"Error with URL :{url}, {e}"})


async def get_api_profile(telegram_id):
    url = f"{BASE_URL}internal_api/users/profile/?telegram_id={telegram_id}"
    async with aiohttp.ClientSession() as session:
        return await error_middleware(session, url)


async def get_api_orders_today():
    url = f"{BASE_URL}internal_api/orders/today/"
    async with aiohttp.ClientSession() as session:
        return await error_middleware(session, url)


async def completed_order(order_id):
    url = f"{BASE_URL}internal_api/orders/{order_id}/completed/"
    async with aiohttp.ClientSession() as session:
        return await error_middleware(session, url)


async def inprogress_order(order_id):
    url = f"{BASE_URL}internal_api/orders/{order_id}/inprogress/"
    async with aiohttp.ClientSession() as session:
        return await error_middleware(session, url)


async def canceled_order(order_id):
    url = f"{BASE_URL}internal_api/orders/{order_id}/canceled/"
    async with aiohttp.ClientSession() as session:
        return await error_middleware(session, url)
