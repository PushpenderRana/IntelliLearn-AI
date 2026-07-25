import streamlit as st
from utils.session import api
from services.api import APIError
from components.ui import section_header, error_banner


def render():
    section_header("📚 AI Notes", "Structured, headings + bullet-point notes with key concepts.")

    if not st.session_state.document_id:
        st.warning("Upload a document first from **Upload Document**.")
        return

    topic = st.text_input("Topic / focus (optional)", placeholder="e.g. entire document, chapter 2...")

    if st.button("✨  Generate Notes", use_container_width=True):
        with st.spinner("Generating notes..."):
            try:
                result = api().notes(st.session_state.document_id, topic or "entire document")
                st.session_state["notes_text"] = result.get("notes", "")
            except APIError as e:
                error_banner(f"Notes generation failed: {e.message}")

    text = st.session_state.get("notes_text")
    if text:
        st.markdown(f'<div class="glass-card">{text}</div>', unsafe_allow_html=True)
        st.download_button("⬇  Download Notes", text, file_name="notes.md", use_container_width=True)
