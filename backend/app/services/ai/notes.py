from app.prompts.notes_prompt import NOTES_PROMPT
from app.services.rag.base_service import BaseRAGService


class NotesService(BaseRAGService):
    def generate_notes(self, document_id: str, topic: str):
        return self.generate(
            document_id=document_id,
            query=topic,
            prompt_template=NOTES_PROMPT
        )