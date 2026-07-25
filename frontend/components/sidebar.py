import streamlit as st
from utils.session import api

NAV_ITEMS = [
    ("🏠", "Dashboard"),
    ("📄", "Upload Document"),
    ("💬", "AI Chat"),
    ("📝", "Summary"),
    ("📚", "Notes"),
    ("❓", "Quiz"),
    ("👤", "Profile"),
    ("⚙", "Settings"),
    ("ℹ", "About IntelliLearn AI"),
]




def render_sidebar():
    with st.sidebar:
        st.markdown("## 🧠 IntelliLearn AI")
        user = st.session_state.get("user") or {}
        if user:
            st.caption(f"Signed in as **{user.get('name', user.get('email', 'User'))}**")
        st.markdown("---")

        for icon, label in NAV_ITEMS:
            active = st.session_state.page == label
            if st.button(f"{icon}  {label}", key=f"nav_{label}", use_container_width=True,
                         type="primary" if active else "secondary"):
                st.session_state.page = label
                st.rerun()

        st.markdown("---")
        theme_label = "🌙 Dark" if st.session_state.theme == "dark" else "☀ Light"
        if st.button(f"Switch to {'Light' if st.session_state.theme == 'dark' else 'Dark'} ({theme_label})",
                     use_container_width=True):
            st.session_state.theme = "light" if st.session_state.theme == "dark" else "dark"
            st.rerun()

        if st.button("🚪  Logout", use_container_width=True):
            try:
                api().logout()
            except Exception:
                pass
            st.session_state.authenticated = False
            st.session_state.user = None
            st.session_state.token = None
            st.session_state.page = "Dashboard"
            st.rerun()
