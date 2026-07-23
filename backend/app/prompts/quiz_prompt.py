from app.services.rag.base_service import BaseRAGService


QUIZ_PROMPT = """
Using only the context below, generate 10 multiple-choice questions.

Context:
{context}

Topic:
{query}

Quiz:
"""


class QuizService(BaseRAGService):
    def generate_quiz(self, topic: str):
        return self.generate(topic, QUIZ_PROMPT)