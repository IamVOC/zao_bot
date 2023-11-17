from vkbottle.bot import Bot, Message

from app.services.ai_service import AIService

from app.config import VK_TOKEN


vkbot = Bot(token=VK_TOKEN)

@vkbot.on.message()
async def main_vk_route(message: Message):
    service = AIService()
    response = service.execute(
                message=message.text,
                chat_id=message.from_id)
    await message.answer(response)
    

