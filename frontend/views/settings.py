import streamlit as st
from components.ui import section_header
from config.settings import API_BASE_URL


def render():
    section_header("⚙ Settings")

    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.markdown("###### Appearance")
    theme = st.radio("Theme", ["dark", "light"], index=0 if st.session_state.theme == "dark" else 1,
                      horizontal=True, format_func=lambda t: "🌙 Dark" if t == "dark" else "☀ Light")
    if theme != st.session_state.theme:
        st.session_state.theme = theme
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.markdown("###### Backend")
    st.text_input("API Base URL", value=API_BASE_URL, disabled=True,
                  help="Set via INTELLILEARN_API_URL environment variable.")
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.markdown("###### Data")
    if st.button("🗑 Clear local session data (chat, quiz, flashcards)"):
        for key in ("chat_history", "flashcards", "quiz_data", "quiz_answers"):
            st.session_state[key] = [] if isinstance(st.session_state.get(key), list) else None
        st.success("Cleared.")
    st.markdown('</div>', unsafe_allow_html=True)
