import streamlit as st
from components.ui import section_header
from config.settings import APP_NAME


def render():
    section_header(f"ℹ About {APP_NAME}")

    st.markdown(f"""
    <div class="glass-card">
    <h4>What is {APP_NAME}?</h4>
    <p>{APP_NAME} is an AI-powered personalized learning platform. Upload a PDF or DOCX
    and it turns into a chattable, quizzable, summarizable study companion — powered by
    Retrieval-Augmented Generation (RAG).</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="glass-card">
    <h4>How RAG Works</h4>
    <p>Your document is split into chunks, converted into embeddings, and stored in a
    vector database. When you ask a question, the most relevant chunks are retrieved and
    passed to the language model as context — so answers stay grounded in your document
    instead of relying purely on the model's memory.</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="glass-card">
    <h4>The AI Pipeline</h4>
    <pre style="white-space:pre-wrap;">
Upload PDF / DOCX
      ↓
Document Loader (PyPDF / DOCX Loader)
      ↓
Text Splitter (LangChain)
      ↓
Embedding Model (nomic-embed-text)
      ↓
FAISS Vector Store
      ↓
Retriever
      ↓
LLM (Ollama Cloud — MiniMax-M3 / Nemotron-3-Super)
      ↓
Generated Response
    </pre>
    </div>
    """, unsafe_allow_html=True)

    cols = st.columns(2)
    with cols[0]:
        st.markdown("""
        <div class="glass-card">
        <h4>How Google OAuth Works</h4>
        <p>Signing in redirects you to Google, which authenticates you and hands
        control back to the backend. The backend stores your profile in a server-side
        session, which secures endpoints like document upload.</p>
        </div>
        """, unsafe_allow_html=True)
        st.markdown("""
        <div class="glass-card">
        <h4>How Summary Generation Works</h4>
        <p>The retriever pulls the most relevant chunks for your topic, and the LLM
        condenses them into a focused summary.</p>
        </div>
        """, unsafe_allow_html=True)
        st.markdown("""
        <div class="glass-card">
        <h4>How Flashcards Work</h4>
        <p>Key terms and concepts are extracted from retrieved chunks and formatted
        as front/back flashcard pairs for spaced revision.</p>
        </div>
        """, unsafe_allow_html=True)
    with cols[1]:
        st.markdown("""
        <div class="glass-card">
        <h4>How AI Chat Works</h4>
        <p>Every question is answered using content retrieved specifically from your
        uploaded document, keeping responses grounded and relevant.</p>
        </div>
        """, unsafe_allow_html=True)
        st.markdown("""
        <div class="glass-card">
        <h4>How Quiz Generation Works</h4>
        <p>Based on your chosen topic, difficulty, and question count, the LLM drafts
        multiple-choice questions with a marked correct answer sourced from your document.</p>
        </div>
        """, unsafe_allow_html=True)
