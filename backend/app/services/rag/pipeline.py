from app.services.document.document_loader import load_document
from app.services.rag.text_splitter import split_documents
from app.services.rag.vector_store import create_vector_store
from app.services.rag.retriever import create_retriever


class RAGPipeline:
    def __init__(self):
        self.retrievers = {}

    def index_document(self, document_id: str, file_path: str):
        documents = load_document(file_path)

        chunks = split_documents(documents)

        vector_store = create_vector_store(chunks)

        retriever = create_retriever(vector_store)

        self.retrievers[document_id] = retriever


    def retrieve(self, document_id: str, query: str):
        retriever = self.retrievers.get(document_id)
        if retriever is None:
            raise ValueError("Document not indexed.")
        return retriever.invoke(query)