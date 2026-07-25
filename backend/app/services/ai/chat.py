from app.prompts.chat_prompt import CHAT_PROMPT
from app.services.rag.base_service import BaseRAGService


class ChatService(BaseRAGService):
    def ask(self, document_id: str, question: str):
        return self.generate(
            document_id=document_id,
            query=question,
            prompt_template=CHAT_PROMPT
        )


