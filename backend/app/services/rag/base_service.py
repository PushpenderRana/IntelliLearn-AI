from app.services.llm.llm import llm
from app.services.rag.pipeline import RAGPipeline


class BaseRAGService:
    def __init__(self, rag_pipeline: RAGPipeline):
        self.rag = rag_pipeline

    def generate(self, query: str, prompt_template: str):
        documents = self.rag.retrieve(query)

        context = "\n\n".join(
            document.page_content
            for document in documents
        )

        prompt = prompt_template.format(
            context=context,
            query=query
        )

        response = llm.invoke(prompt)

        return response.content