from langchain_community.vectorstores import FAISS

from app.services.rag.embedding import embeddings


def create_vector_store(chunks):
    return FAISS.from_documents(
        documents=chunks,
        embedding=embeddings
    )