from langchain_groq import ChatGroq

from app.config.settings import settings


class LLMService:
    def __init__(self):
        self.primary_llm = ChatGroq(
            model=settings.PRIMARY_MODEL,
            api_key=settings.GROQ_API_KEY
        )

        self.fallback_llm = ChatGroq(
            model=settings.FALLBACK_MODEL,
            api_key=settings.GROQ_API_KEY
        )

    def invoke(self, prompt: str):
        try:
            return self.primary_llm.invoke(prompt)
        except Exception as error:
            print(f"Primary model failed: {error}")
            return self.fallback_llm.invoke(prompt)


llm = LLMService()