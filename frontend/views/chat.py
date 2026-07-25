import streamlit as st
from utils.session import api, bump_stat
from services.api import APIError
from components.ui import section_header, error_banner

SUGGESTED = [
    "Summarize the key ideas in this document.",
    "What are the most important terms defined here?",
    "Explain this document to me like I'm a beginner.",
]


def render():
    section_header("💬 AI Chat", "Ask anything about your uploaded document.")

    if not st.session_state.document_id:
        st.warning("Upload a document first from **Upload Document**.")
        return

    top = st.columns([4, 1])
    with top[1]:
        if st.button("🗑 Clear Chat", use_container_width=True):
            st.session_state.chat_history = []
            st.rerun()

    st.markdown("###### Suggested questions")
    sc = st.columns(len(SUGGESTED))
    for col, q in zip(sc, SUGGESTED):
        with col:
            if st.button(q, key=f"sug_{q}", use_container_width=True):
                _ask(q)

    for msg in st.session_state.chat_history:
        css_class = "chat-bubble-user" if msg["role"] == "user" else "chat-bubble-ai"
        st.markdown(f'<div class="{css_class}">{msg["content"]}</div>', unsafe_allow_html=True)

    question = st.chat_input("Type your question...")
    if question:
        _ask(question)


def _ask(question: str):
    st.session_state.chat_history.append({"role": "user", "content": question})
    with st.spinner("Thinking..."):
        try:
            result = api().chat(st.session_state.document_id, question)
            answer = result.get("answer", "")
            st.session_state.chat_history.append({"role": "ai", "content": answer})
            bump_stat("questions_asked")
        except APIError as e:
            error_banner(f"Chat failed: {e.message}")
    st.rerun()
