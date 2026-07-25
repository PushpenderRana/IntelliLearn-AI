import streamlit as st
from utils.session import api
from services.api import APIError
from components.ui import section_header, error_banner


def render():
    section_header("📝 AI Summary", "Generate a concise summary of your document.")

    if not st.session_state.document_id:
        st.warning("Upload a document first from **Upload Document**.")
        return

    topic = st.text_input("Topic / focus (optional)", placeholder="e.g. entire document, chapter 3, key definitions...")

    c1, c2 = st.columns([1, 1])
    generate = c1.button("✨  Generate Summary", use_container_width=True)
    regenerate = c2.button("🔄  Regenerate", use_container_width=True)

    if generate or regenerate:
        with st.spinner("Generating summary..."):
            try:
                result = api().summary(st.session_state.document_id, topic or "entire document")
                st.session_state["summary_text"] = result.get("summary", "")
            except APIError as e:
                error_banner(f"Summary generation failed: {e.message}")

    text = st.session_state.get("summary_text")
    if text:
        st.markdown(f'<div class="glass-card">{text}</div>', unsafe_allow_html=True)
        c1, c2 = st.columns(2)
        with c1:
            st.code(text, language=None)
            st.caption("Select the box above and copy.")
        with c2:
            st.download_button("⬇  Download Summary", text, file_name="summary.txt", use_container_width=True)
