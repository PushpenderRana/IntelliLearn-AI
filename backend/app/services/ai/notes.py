from app.prompts.notes_prompt import NOTES_PROMPT
from app.services.rag.base_service import BaseRAGService


class NotesService(BaseRAGService):
    def generate_notes(self, topic: str):
        return self.generate(topic, NOTES_PROMPT)