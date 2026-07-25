import streamlit as st

from config.settings import APP_NAME
from utils.session import init_state, api
from utils.styles import inject_css
from components.sidebar import render_sidebar

from views import login, dashboard, upload, chat, summary, notes, quiz, profile, settings, about

st.set_page_config(
    page_title=APP_NAME,
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded",
)

init_state()
inject_css(st.session_state.theme)

# /auth/callback redirects here with ?code=<temp_code> (never the raw JWT).
# Trade it in for the real access_token, store that, scrub the URL.
incoming_code = st.query_params.get("code")
if incoming_code and not st.session_state.authenticated:
    try:
        exchange_result = api().exchange_code(incoming_code)
        st.session_state.token = exchange_result.get("access_token")
        me = api().get_me()
        if me.get("authenticated"):
            st.session_state.authenticated = True
            st.session_state.user = me.get("user")
    except Exception as e:
        st.session_state.auth_error = str(e)
    st.query_params.clear()
    st.rerun()

# Re-apply a token already captured earlier this session (e.g. after a
# page rerun) since api_client itself doesn't persist across reruns
# unless session_state already holds the constructed instance — it does,
# but this covers the case where set_token wasn't called yet this run.
if st.session_state.token and not api().is_authenticated:
    api().set_token(st.session_state.token)

if not st.session_state.authenticated:
    login.render()
    st.stop()

render_sidebar()

PAGES = {
    "Dashboard": dashboard.render,
    "Upload Document": upload.render,
    "AI Chat": chat.render,
    "Summary": summary.render,
    "Notes": notes.render,
    "Quiz": quiz.render,

    "Profile": profile.render,
    "Settings": settings.render,
    "About IntelliLearn AI": about.render,
}


PAGES.get(st.session_state.page, dashboard.render)()
