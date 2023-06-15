

def get_order_info(order):
    id = order.id
    type_payment_display = order.get_type_payment_display()
    status_display = order.get_status_display()
    address_display = order.address
    price = order.price
    order_display = f"ID:{id}, Статус:{status_display} \n" \
                    f"Цена:{price}р, Оплата: {type_payment_display} \n" \
                    f"Адрес: {address_display} \n"
    if description := order.description:
        order_display +=f"Описание: {description}"
    return order_display
