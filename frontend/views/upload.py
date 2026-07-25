import time
import streamlit as st
from utils.session import api, bump_stat
from services.api import APIError
from components.ui import success_banner, error_banner, section_header


def render():
    section_header("📄 Upload Document", "Supports PDF and DOCX — indexed automatically for chat, summary, notes, quiz & flashcards.")

    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    file = st.file_uploader("Drag & drop or browse", type=["pdf", "docx"])

    if file is not None:
        st.write(f"**{file.name}**  ·  {round(len(file.getvalue()) / 1024, 1)} KB")

        if st.button("🚀  Upload & Index", use_container_width=True):
            progress = st.progress(0, text="Uploading...")
            for pct in (20, 45, 70):
                time.sleep(0.15)
                progress.progress(pct, text="Uploading...")

            content_type = (
                "application/pdf" if file.name.lower().endswith(".pdf")
                else "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
            )
            try:
                progress.progress(85, text="Indexing document...")
                result = api().upload_document(file.name, file.getvalue(), content_type)
                progress.progress(100, text="Done")
                time.sleep(0.2)
                progress.empty()

                st.session_state.document_info = {
                    "filename": result.get("filename", file.name),
                    "size_kb": round(len(file.getvalue()) / 1024, 1),
                }
                st.session_state.document_id = result.get("document_id")
                bump_stat("documents")
                success_banner(result.get("message", "Document uploaded and indexed successfully."))
                st.balloons()
            except APIError as e:
                progress.empty()
                if e.status_code == 401:
                    error_banner("You need to be signed in to upload. Please log in first.")
                else:
                    error_banner(f"Upload failed: {e.message}")
    st.markdown('</div>', unsafe_allow_html=True)

    if st.session_state.document_info:
        info = st.session_state.document_info
        st.markdown("#### Current Document")
        c1, c2 = st.columns(2)
        with c1:
            st.markdown(f"""<div class="glass-card"><b>Filename</b><br>{info['filename']}</div>""",
                        unsafe_allow_html=True)
        with c2:
            st.markdown(f"""<div class="glass-card"><b>Size</b><br>{info['size_kb']} KB</div>""",
                        unsafe_allow_html=True)
