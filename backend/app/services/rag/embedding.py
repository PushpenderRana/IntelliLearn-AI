from langchain_ollama import OllamaEmbeddings

from app.config.settings import settings


embeddings = OllamaEmbeddings(
    model=settings.EMBEDDING_MODEL,
)