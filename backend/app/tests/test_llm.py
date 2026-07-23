# test pdf loader
# from app.services.document.pdf_loader import load_pdf


# def main():
#     documents = load_pdf("backend/app/tests/sample.pdf")

#     print(f"Total Pages: {len(documents)}")

#     print("\nFirst Page Content:\n")
#     print(documents[0].page_content)


# if __name__ == "__main__":
#     main()

# test docx loader
# from app.services.document.docx_loader import load_docx


# def main():
#     documents = load_docx("backend/app/tests/sample.docx")

#     print(f"Total Documents: {len(documents)}")

#     print("\nContent:\n")
#     print(documents[0].page_content)


# if __name__ == "__main__":
#     main()

# from app.services.document.document_loader import load_document


# def main():
#     file_path = "backend/app/tests/sample.pdf"

#     documents = load_document(file_path)

#     print(f"Total Documents: {len(documents)}")
#     print(documents[0].page_content)


# if __name__ == "__main__":
#     main()

# from app.services.document.document_loader import load_document
# from app.services.rag.text_splitter import split_documents


# def main():
#     documents = load_document("backend/app/tests/sample.pdf")

#     chunks = split_documents(documents)

#     print(f"Original Documents : {len(documents)}")
#     print(f"Total Chunks : {len(chunks)}")

#     print("\nFirst Chunk:\n")
#     print(chunks[0].page_content)

#     print("\nMetadata:\n")
#     print(chunks[0].metadata)


# if __name__ == "__main__":
#     main()

# from app.services.rag.embedding import embeddings


# def main():
#     vector = embeddings.embed_query(
#         "Artificial Intelligence is changing the world."
#     )

#     print(f"Vector Length: {len(vector)}")

#     print("\nFirst 10 Values:\n")

#     print(vector[:10])


# if __name__ == "__main__":
#     main()

# from app.services.document.document_loader import load_document
# from app.services.rag.text_splitter import split_documents
# from app.services.rag.vector_store import create_vector_store


# def main():
#     documents = load_document("backend/app/tests/sample.pdf")

#     chunks = split_documents(documents)

#     vector_store = create_vector_store(chunks)

#     print(vector_store.index.ntotal)


# if __name__ == "__main__":
#     main()

# from app.services.document.document_loader import load_document
# from app.services.rag.text_splitter import split_documents
# from app.services.rag.vector_store import create_vector_store
# from app.services.rag.retriever import create_retriever


# def main():
#     documents = load_document("backend/app/tests/sample.pdf")

#     chunks = split_documents(documents)

#     vector_store = create_vector_store(chunks)

#     retriever = create_retriever(vector_store)

#     results = retriever.invoke("skills")

#     print(f"Retrieved Chunks: {len(results)}")

#     print("\nFirst Retrieved Chunk:\n")
#     print(results[0].page_content)

#     print("\nMetadata:\n")
#     print(results[0].metadata)


# if __name__ == "__main__":
#     main()

# from app.services.rag.pipeline import RAGPipeline


# def main():
#     rag = RAGPipeline("backend/app/tests/sample.pdf")

#     results = rag.retrieve(
#         "What is Artificial Intelligence?"
#     )

#     print(f"Retrieved Chunks: {len(results)}")

#     print("\nBest Match:\n")

#     print(results[0].page_content)

#     print("\nMetadata:\n")

#     print(results[0].metadata)


# if __name__ == "__main__":
#     main()

from app.services.summary.summary import SummaryService


def main():
    summary = SummaryService(
        "backend/app/tests/sample.pdf"
    )

    result = summary.generate(
        "Artificial Intelligence"
    )

    print(result)


if __name__ == "__main__":
    main()

