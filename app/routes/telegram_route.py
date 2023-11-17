from aiogram import Bot, Dispatcher
from aiogram.types import Message

from app.services.ai_service import AIService

from app.config import TG_TOKEN


tgbot = Bot(token=TG_TOKEN)
dp = Dispatcher(tgbot)

@dp.message_handler(content_types=['text'])
async def main_tg_route(message: Message):
    service = AIService()
    response = service.execute(
                message=message.text,
                chat_id=message.from_user.id)
    await message.answer(response)

