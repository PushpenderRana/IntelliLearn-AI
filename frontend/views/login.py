import streamlit as st
from utils.session import api
from config.settings import APP_NAME, APP_TAGLINE


def render():
    if st.session_state.get("auth_error"):
        st.error(f"Sign-in failed: {st.session_state.auth_error}")
        st.session_state.auth_error = None

    st.markdown(f"""
    <div class="hero">
        <h1><span class="gradient-text">{APP_NAME}</span></h1>
        <p>{APP_TAGLINE}</p>
    </div>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        st.markdown('<div class="glass-card" style="text-align:center;">', unsafe_allow_html=True)
        st.markdown("#### Sign in to continue")
        st.link_button("🔐  Continue with Google", api().login_url(), use_container_width=True)
        st.caption("Opens Google sign-in. After you sign in, you'll land back here already logged in — "
                   "no extra click needed.")
        st.markdown('</div>', unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    c1, c2, c3, c4, c5 = st.columns(5)
    features = [
        ("💬", "AI Chat"), ("📝", "AI Summary"), ("📚", "AI Notes"),
        ("❓", "AI Quiz"), ("📈", "Analytics"),
    ]
    for col, (icon, label) in zip([c1, c2, c3, c4, c5], features):

        with col:
            st.markdown(f"""<div class="glass-card" style="text-align:center;">
                <div style="font-size:1.6rem;">{icon}</div>
                <div style="font-size:.8rem; margin-top:.3rem;">{label}</div>
            </div>""", unsafe_allow_html=True)
