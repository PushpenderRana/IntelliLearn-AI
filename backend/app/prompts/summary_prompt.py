from app.services.rag.base_service import BaseRAGService


SUMMARY_PROMPT = """
You are an expert teacher.

Using only the context below, generate a detailed study summary.

Context:
{context}

Topic:
{query}

Summary:
"""


class SummaryService(BaseRAGService):
    def generate_summary(self, topic: str):
        return self.generate(topic, SUMMARY_PROMPT)