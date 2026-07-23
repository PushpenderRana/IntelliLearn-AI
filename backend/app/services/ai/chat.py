from app.prompts.chat_prompt import CHAT_PROMPT
from app.services.rag.base_service import BaseRAGService


class ChatService(BaseRAGService):
    def ask(self, question: str):
        return self.generate(question, CHAT_PROMPT)