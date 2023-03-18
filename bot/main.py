from aiogram import executor
from drivers.handlers import send_orders
from config import dp, TIME_UPDATE_ORDERS

import drivers
import asyncio
import aioschedule

async def scheduler():
    aioschedule.every(TIME_UPDATE_ORDERS).minutes.do(send_orders)
    while True:
        await aioschedule.run_pending()
        await asyncio.sleep(1)

async def on_startup(_):
    asyncio.create_task(scheduler())

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=False, on_startup=on_startup)
