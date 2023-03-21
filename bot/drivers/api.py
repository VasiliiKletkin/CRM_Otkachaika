import os

import aiohttp

BASE_URL = os.environ.get('BASE_URL')


async def get_api_profile(telegram_id):
    url = f"{BASE_URL}internal_api/users/profile/?telegram_id={telegram_id}"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            return await resp.json()


async def get_api_orders_today():
    url = f"{BASE_URL}internal_api/orders/today/"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            return await resp.json()


async def completed_order(order_id):
    url = f"{BASE_URL}internal_api/orders/{order_id}/completed/"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            return await resp.json()


async def inprogress_order(order_id):
    url = f"{BASE_URL}internal_api/orders/{order_id}/inprogress/"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            return await resp.json()


async def canceled_order(order_id):
    url = f"{BASE_URL}internal_api/orders/{order_id}/canceled/"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            return await resp.json()
