import hashlib
from app.services.llm.llm import llm
from app.services.rag.pipeline import RAGPipeline
from app.services.ai.cache_service import cache_service


class BaseRAGService:
    def __init__(self, rag_pipeline: RAGPipeline):
        self.rag = rag_pipeline

    def _build_cache_key(self, document_id: str, query: str, prompt_template: str, **kwargs) -> str:
        normalized_query = query.strip().lower()
        kwargs_str = str(sorted(kwargs.items()))
        raw = f"{document_id}|{normalized_query}|{prompt_template}|{kwargs_str}"
        return f"rag:{hashlib.md5(raw.encode('utf-8')).hexdigest()}"

    def generate(
        self,
        document_id: str,
        query: str,
        prompt_template: str,
        **kwargs
    ):
        cache_key = self._build_cache_key(document_id, query, prompt_template, **kwargs)
        cached_response = cache_service.get(cache_key)
        if cached_response is not None:
            return cached_response

        documents = self.rag.retrieve(
            document_id=document_id,
            query=query
        )

        context = "\n\n".join(
            document.page_content
            for document in documents
        )

        prompt = prompt_template.format(
            context=context,
            query=query,
            **kwargs
        )

        response = llm.invoke(prompt)
        output = response.content

        cache_service.set(cache_key, output)

        return output