from app.prompts.quiz_prompt import QUIZ_PROMPT
from app.services.rag.base_service import BaseRAGService


class QuizService(BaseRAGService):
    def generate_quiz(self, topic: str):
        return self.generate(topic, QUIZ_PROMPT)