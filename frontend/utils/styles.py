import streamlit as st
from config.settings import THEME_COLORS


def inject_css(theme: str = "dark"):
    c = THEME_COLORS[theme]
    st.markdown(f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700;800&family=Inter:wght@400;500;600&display=swap');

    html, body, [class*="css"] {{
        font-family: 'Inter', sans-serif;
    }}

    .stApp {{
        background: {c['bg']};
        background-image:
            radial-gradient(at 10% 0%, {c['gradient_start']}22 0px, transparent 50%),
            radial-gradient(at 90% 10%, {c['gradient_end']}22 0px, transparent 50%);
        color: {c['text']};
    }}

    h1, h2, h3, h4 {{
        font-family: 'Poppins', sans-serif;
        color: {c['text']};
    }}

    .gradient-text {{
        background: linear-gradient(90deg, {c['gradient_start']}, {c['gradient_end']});
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: 800;
    }}

    .glass-card {{
        background: {c['glass']};
        border: 1px solid {c['glass_border']};
        border-radius: 20px;
        padding: 1.4rem 1.6rem;
        backdrop-filter: blur(14px);
        -webkit-backdrop-filter: blur(14px);
        box-shadow: 0 8px 32px rgba(0,0,0,0.18);
        transition: transform .25s ease, box-shadow .25s ease;
        margin-bottom: 1rem;
    }}
    .glass-card:hover {{
        transform: translateY(-4px);
        box-shadow: 0 14px 40px rgba(0,0,0,0.28);
    }}

    .stat-value {{
        font-size: 2rem;
        font-weight: 800;
        font-family: 'Poppins', sans-serif;
        background: linear-gradient(90deg, {c['gradient_start']}, {c['gradient_end']});
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }}
    .stat-label {{
        color: {c['text_muted']};
        font-size: .85rem;
        font-weight: 500;
    }}

    .hero {{
        text-align: center;
        padding: 3rem 1rem 2rem 1rem;
    }}
    .hero h1 {{
        font-size: 3rem;
        margin-bottom: .3rem;
    }}
    .hero p {{
        color: {c['text_muted']};
        font-size: 1.15rem;
    }}

    div.stButton > button {{
        border-radius: 12px;
        border: 1px solid {c['glass_border']};
        background: linear-gradient(90deg, {c['gradient_start']}, {c['gradient_end']});
        color: white;
        font-weight: 600;
        padding: .5rem 1.2rem;
        transition: transform .15s ease, box-shadow .15s ease;
    }}
    div.stButton > button:hover {{
        transform: translateY(-2px) scale(1.02);
        box-shadow: 0 6px 18px {c['gradient_start']}55;
    }}

    section[data-testid="stSidebar"] {{
        background: {c['bg_secondary']};
        border-right: 1px solid {c['glass_border']};
    }}

    .chat-bubble-user {{
        background: linear-gradient(90deg, {c['gradient_start']}, {c['gradient_end']});
        color: white;
        border-radius: 16px 16px 4px 16px;
        padding: .7rem 1rem;
        margin: .4rem 0;
        max-width: 75%;
        margin-left: auto;
    }}
    .chat-bubble-ai {{
        background: {c['glass']};
        border: 1px solid {c['glass_border']};
        border-radius: 16px 16px 16px 4px;
        padding: .7rem 1rem;
        margin: .4rem 0;
        max-width: 75%;
    }}

    .flashcard {{
        background: linear-gradient(135deg, {c['gradient_start']}, {c['gradient_end']});
        border-radius: 20px;
        color: white;
        min-height: 220px;
        display: flex;
        align-items: center;
        justify-content: center;
        text-align: center;
        font-size: 1.3rem;
        font-weight: 600;
        padding: 2rem;
        box-shadow: 0 10px 30px {c['gradient_start']}44;
    }}

    .badge {{
        display: inline-block;
        padding: .2rem .7rem;
        border-radius: 999px;
        font-size: .75rem;
        font-weight: 600;
        background: {c['glass']};
        border: 1px solid {c['glass_border']};
    }}
    .badge-success {{ color: {c['success']}; border-color: {c['success']}55; }}
    .badge-error {{ color: {c['error']}; border-color: {c['error']}55; }}

    #MainMenu, footer {{visibility: hidden;}}
    </style>
    """, unsafe_allow_html=True)
