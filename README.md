# IntelliLearn AI

IntelliLearn AI is an AI-powered study assistant. Upload your notes or documents and it turns them into a searchable knowledge base you can chat with, quiz yourself on, and summarize.

## Features

- **RAG Pipeline** - Documents are chunked, embedded, and stored in a vector store (FAISS) so answers are grounded in your actual uploaded content.
- **AI Chat** - Ask questions about your uploaded material and get context-aware answers powered by an LLM (Google Gemini / Ollama support via LangChain).
- **Quiz Generator** - Automatically generates quizzes from your documents to test your understanding.
- **Summary Generator** - Produces concise summaries of uploaded notes or documents.
- **Notes Support** - Structured notes generation from raw content.
- **Authentication** - JWT + OAuth based user login.

## Tech Stack

**Backend**
- FastAPI
- LangChain + LangGraph
- FAISS (vector store)
- Sentence Transformers (embeddings)
- SQLAlchemy
- JWT / OAuth2

**Frontend**
- Streamlit
- Plotly

## Project Structure

```
backend/
  app/
    api/routes/       # chat, quiz, summary, notes, upload, auth endpoints
    auth/              # JWT, OAuth, security
    services/
      rag/             # embedding, vector store, retriever, pipeline
      ai/              # chat, quiz, summary, notes logic
      document/        # PDF/DOCX loaders
      llm/             # LLM integration
    prompts/           # prompt templates
    schemas/           # request/response models

frontend/
  app.py
  views/               # chat, quiz, summary, notes, upload, dashboard, login
  components/
  services/
```

## Getting Started

### Backend
```bash
cd backend
pip install -r requirements.txt
uvicorn app.main:app --reload
```

### Frontend
```bash
cd frontend
pip install -r requirements.txt
streamlit run app.py
```

## How It Works

1. Upload a document (PDF/DOCX).
2. It's split into chunks and embedded into a vector store.
3. Chat, quiz, and summary features retrieve relevant chunks (RAG) and pass them to the LLM to generate grounded responses.

