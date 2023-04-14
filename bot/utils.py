from drivers.api import get_api_profile, get_api_orders_today

async def is_driver(telegram_id):
    profile = await get_api_profile(telegram_id)
    return profile if profile.get("user_type") == "DRIVER" else None

async def get_orders_today():
    response = await get_api_orders_today()
    if not response: response = []
    return response


def get_order_info(order):
    id = order.get('id')
    address = order.get('address')
    type_payment_display = order.get('type_payment_display')
    address_display = address.get('address_display')
    price = order.get('price')
    description = order.get('description')
    order_display = f"ID:{id}, Оплата:{type_payment_display}, Цена:{price}р \n" \
                    f"{address_display} \n"
    if description:
        order_display +=f" {description}"
    return order_display
