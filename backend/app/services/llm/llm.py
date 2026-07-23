from langchain_ollama import ChatOllama

from app.config.settings import settings


class LLMService:
    def __init__(self):
        self.primary_llm = ChatOllama(
            model=settings.PRIMARY_MODEL,
        )

        self.fallback_llm = ChatOllama(
            model=settings.FALLBACK_MODEL,
        )

    def invoke(self, prompt: str):
        try:
            return self.primary_llm.invoke(prompt)
        except Exception as error:
            print(f"Primary model failed: {error}")
            return self.fallback_llm.invoke(prompt)


llm = LLMService()