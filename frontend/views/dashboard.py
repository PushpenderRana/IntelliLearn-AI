import streamlit as st
from components.ui import stat_card, feature_card
from config.settings import APP_NAME, APP_TAGLINE

FEATURES = [
    ("💬", "AI Chat", "Ask questions about your uploaded document."),
    ("📝", "AI Summary", "Get instant, topic-aware summaries."),
    ("📚", "AI Notes", "Structured notes with key concepts."),
    ("❓", "AI Quiz", "Auto-generated MCQs to test yourself."),
    ("📈", "Learning Analytics", "Track progress over time."),
]


def render():
    st.markdown(f"""
    <div class="hero">
        <h1><span class="gradient-text">{APP_NAME}</span></h1>
        <p>{APP_TAGLINE}</p>
    </div>
    """, unsafe_allow_html=True)

    stats = st.session_state.stats
    cols = st.columns(4)
    values = [
        ("Documents", stats["documents"]),
        ("Questions Asked", stats["questions_asked"]),
        ("Quizzes Generated", stats["quizzes_generated"]),
        ("Study Time (min)", stats["study_minutes"]),
    ]
    for col, (label, val) in zip(cols, values):
        with col:
            stat_card(label, val)

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("#### Explore")
    row1 = st.columns(3)
    row2 = st.columns(3)
    for col, (icon, title, desc) in zip(row1 + row2, FEATURES):
        with col:
            feature_card(icon, title, desc)

    if not st.session_state.document_info:
        st.info("📄 No document uploaded yet — head to **Upload Document** to get started.")
