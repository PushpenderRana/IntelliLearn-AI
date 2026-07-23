from app.services.rag.base_service import BaseRAGService


CHAT_PROMPT = """
You are an AI tutor.

Answer the student's question using only the context below.

Context:
{context}

Question:
{query}

Answer:
"""


class ChatService(BaseRAGService):
    def ask(self, question: str):
        return self.generate(question, CHAT_PROMPT)