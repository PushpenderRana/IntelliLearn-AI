import streamlit as st
from services.api import APIClient


def init_state():
    defaults = {
        "api_client": APIClient(),
        "authenticated": False,
        "user": None,
        "token": None,
        "auth_error": None,
        "theme": "dark",
        "page": "Dashboard",
        "chat_history": [],          # list of {"role": "user"/"ai", "content": str}
        "document_info": None,       # {"filename", "size_kb"}
        "document_id": None,         # backend is multi-doc now, every content call needs this
        "quiz_data": None,
        "quiz_index": 0,
        "quiz_score": 0,
        "quiz_answers": [],
        "stats": {
            "documents": 0,
            "questions_asked": 0,
            "quizzes_generated": 0,
            "study_minutes": 0,
        },
    }
    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value


def bump_stat(key, amount=1):
    st.session_state.stats[key] = st.session_state.stats.get(key, 0) + amount


def api() -> APIClient:
    client = st.session_state.get("api_client")
    if client is None or not hasattr(client, "submit_quiz"):
        token = getattr(client, "token", None) or st.session_state.get("token")
        new_client = APIClient()
        if token:
            new_client.set_token(token)
        st.session_state.api_client = new_client
        return new_client
    return client


