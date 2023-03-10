from drivers.api import get_profile

async def is_driver(telegram_id):
    profile = await get_profile(telegram_id)
    return profile if profile.get("user_type") == "DRIVER" else None



def get_order_info(order):
    
    id = order.get('id')
    address = order.get('address')
    home = address.get('home')    
    street = address.get('home')    
    city = address.get('city')
    address_display = f"{street} {home} {city}"
    price = order.get('price')
    description = order.get('description')
    date_planned = order.get('date_planned')
    type_payment = order.get('type_payment')

    order_display = f"Заказ:{id}, Цена:{price}р \n" \
                    f"{address_display} \n"
    if description:
        order_display +=f" {description}"
    
    return order_display
