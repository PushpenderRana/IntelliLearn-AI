import streamlit as st


def stat_card(label: str, value):
    st.markdown(f"""
    <div class="glass-card" style="text-align:center;">
        <div class="stat-value">{value}</div>
        <div class="stat-label">{label}</div>
    </div>
    """, unsafe_allow_html=True)


def feature_card(icon: str, title: str, description: str):
    st.markdown(f"""
    <div class="glass-card">
        <div style="font-size:2rem;">{icon}</div>
        <h4 style="margin:.4rem 0 .2rem 0;">{title}</h4>
        <div style="color:var(--text-muted); font-size:.9rem;">{description}</div>
    </div>
    """, unsafe_allow_html=True)


def success_banner(message: str):
    st.markdown(f'<div class="badge badge-success">✅ {message}</div>', unsafe_allow_html=True)
    st.success(message)


def error_banner(message: str):
    st.markdown(f'<div class="badge badge-error">⚠ {message}</div>', unsafe_allow_html=True)
    st.error(message)


def section_header(title: str, subtitle: str = ""):
    st.markdown(f"### {title}")
    if subtitle:
        st.caption(subtitle)
