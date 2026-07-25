import streamlit as st
from components.ui import section_header, stat_card


def render():
    section_header("👤 Profile")

    user = st.session_state.get("user") or {}
    c1, c2 = st.columns([1, 3])
    with c1:
        pic = user.get("picture")
        if pic:
            st.image(pic, width=110)
        else:
            st.markdown('<div class="glass-card" style="text-align:center; font-size:2.5rem;">👤</div>',
                        unsafe_allow_html=True)
    with c2:
        st.markdown(f"""
        <div class="glass-card">
            <b>Name:</b> {user.get('name', '—')}<br>
            <b>Email:</b> {user.get('email', '—')}<br>
            <b>Last Login:</b> {user.get('last_login', 'This session')}
        </div>
        """, unsafe_allow_html=True)

    st.markdown("#### Study Statistics")
    stats = st.session_state.stats
    cols = st.columns(4)
    vals = [
        ("Documents", stats["documents"]), ("Questions Asked", stats["questions_asked"]),
        ("Quizzes", stats["quizzes_generated"]),
        ("Study Min", stats["study_minutes"]),
    ]

    for col, (label, val) in zip(cols, vals):
        with col:
            stat_card(label, val)
