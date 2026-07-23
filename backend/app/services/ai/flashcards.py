from app.prompts.flashcard_prompt import FLASHCARD_PROMPT
from app.services.rag.base_service import BaseRAGService


class FlashcardService(BaseRAGService):
    def generate_flashcards(self, topic: str):
        return self.generate(topic, FLASHCARD_PROMPT)