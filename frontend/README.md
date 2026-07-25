# IntelliLearn AI — Streamlit Frontend

Frontend only. Talks to your existing FastAPI backend through `services/api.py` — no backend code touched.

## Run

```bash
pip install -r requirements.txt
export INTELLILEARN_API_URL=http://localhost:8000   # your FastAPI backend
streamlit run app.py
```

## Structure

```
app.py                 entrypoint, routing, auth gate
config/settings.py      API base URL, endpoint paths, theme colors
services/api.py         every backend call lives here (APIClient)
utils/session.py        st.session_state defaults + helpers
utils/styles.py          glassmorphism / gradient CSS, dark+light theme
components/sidebar.py    nav + theme toggle + logout
components/ui.py         stat cards, feature cards, banners
views/                   one file per page (dashboard, upload, chat, summary,
                         notes, quiz, flashcards, analytics, profile, settings, about)
```

## Endpoints used (exactly as provided, nothing invented)

| Feature | Method | Path |
|---|---|---|
| Login | GET | `/auth/login` |
| OAuth callback | GET | `/auth/callback` |
| Logout | GET | `/auth/logout` |
| Current user | GET | `/auth/me` |
| Upload | POST | `/upload/` (multipart, field `file`) |
| Chat | POST | `/chat/` `{question}` |
| Summary | POST | `/summary/` `{topic}` |
| Notes | POST | `/notes/` `{topic}` |
| Quiz | POST | `/quiz/` `{topic, difficulty, number_of_questions}` |
| Flashcards | POST | `/flashcards/` `{topic}` |

## Auth architecture — JWT bearer token, not cookies

Earlier version relied on `request.session` cookies, which broke because
Google's OAuth consent needs a real browser tab, while API calls come from
Streamlit's own `requests.Session()` — two separate clients, two separate
cookie jars, no way for one to see the other's cookie.

Fixed by switching to JWT:
1. `/auth/login` opens in browser → Google → `/auth/callback`.
2. Callback builds a signed JWT from the Google userinfo and redirects the
   browser to `http://localhost:8501/?token=<jwt>` (see backend
   `app/auth/routes/auth.py`).
3. `app.py` reads `st.query_params["token"]` on load, stores it in
   `st.session_state.token`, pushes it into `APIClient.set_token()`, and
   clears it from the URL.
4. From then on `APIClient` sends `Authorization: Bearer <token>` on every
   call automatically — `get_current_user` on the backend validates it via
   `app/auth/jwt.py`.
5. Logout just drops the token client-side (`api().logout()` also clears it
   from `APIClient`); JWT is stateless so there's nothing to revoke server-side.

Backend files touched: `app/auth/jwt.py` (new), `app/auth/dependencies.py`,
`app/auth/routes/auth.py`. Add `python-jose[cryptography]` to backend
requirements and set `JWT_SECRET_KEY` / `INTELLILEARN_FRONTEND_URL` env vars
— see `requirements-addition.txt` in the backend bundle.

Quiz/notes/flashcards response shapes weren't fully specified by the schema
files, so `views/quiz.py` and `views/flashcards.py` normalize a few likely
shapes (list of dicts, `{"questions": [...]}`, `{"cards": [...]}`, plain
string) — adjust `_normalize()` in each file if your actual schema differs.
