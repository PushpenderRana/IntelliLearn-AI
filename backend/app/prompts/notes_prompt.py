from app.services.rag.base_service import BaseRAGService


NOTES_PROMPT = """
Using only the context below, create concise study notes.

Context:
{context}

Topic:
{query}

Notes:
"""


class NotesService(BaseRAGService):
    def generate_notes(self, topic: str):
        return self.generate(topic, NOTES_PROMPT)