from app.prompts.summary_prompt import SUMMARY_PROMPT
from app.services.rag.base_service import BaseRAGService


class SummaryService(BaseRAGService):
    def generate_summary(self, document_id: str, topic: str):
        return self.generate(
            document_id=document_id,
            query=topic,
            prompt_template=SUMMARY_PROMPT
        )