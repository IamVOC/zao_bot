import requests

from app.config import BOT_GUID, AI_HOST


class AIService:

    def execute(self, message: str, chat_id: int) -> str:
        payload = { 
                   "bot_guid": BOT_GUID,
                   "message": message,
                   "client_id": chat_id,
                  }
        response = requests.post(AI_HOST, json=payload)
        answer = response.json()['answer']
        return answer

