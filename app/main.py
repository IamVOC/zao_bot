import asyncio

from app.routes.vk_route import vkbot
from app.routes.telegram_route import dp


async def main():
    vk = asyncio.create_task(vkbot.run_polling())
    tg = asyncio.create_task(dp.start_polling())
    await vk
    await tg

if __name__ == "__main__":
    asyncio.run(main())

