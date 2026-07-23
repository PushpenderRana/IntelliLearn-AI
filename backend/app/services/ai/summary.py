from app.prompts.summary_prompt import SUMMARY_PROMPT
from app.services.rag.base_service import BaseRAGService


class SummaryService(BaseRAGService):
    def generate_summary(self, topic: str):
        return self.generate(topic, SUMMARY_PROMPT)