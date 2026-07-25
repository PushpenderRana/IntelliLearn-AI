"""
Every request to the FastAPI backend goes through here.

Auth model: JWT bearer token via a code-exchange handshake, not cookies.
/auth/callback redirects the browser to Streamlit with a short-lived
?code=, never the JWT itself. app.py trades that code for the real
token via exchange_code(), which stores it and attaches
`Authorization: Bearer <token>` to every request this client makes
from then on.
"""
import requests

from config.settings import (
    API_BASE_URL, EP_LOGIN, EP_EXCHANGE, EP_LOGOUT, EP_ME, EP_UPLOAD,
    EP_CHAT, EP_SUMMARY, EP_NOTES, EP_QUIZ, REQUEST_TIMEOUT,
)


class APIError(Exception):
    def __init__(self, message, status_code=None):
        super().__init__(message)
        self.message = message
        self.status_code = status_code


class APIClient:
    def __init__(self):
        self.session = requests.Session()
        self.token = None

    # ---------- token management ----------
    def set_token(self, token: str):
        self.token = token
        if token:
            self.session.headers["Authorization"] = f"Bearer {token}"
        else:
            self.session.headers.pop("Authorization", None)

    def clear_token(self):
        self.set_token(None)

    @property
    def is_authenticated(self) -> bool:
        return bool(self.token)

    # ---------- auth ----------
    def login_url(self) -> str:
        return f"{API_BASE_URL}{EP_LOGIN}"

    def exchange_code(self, code: str):
        """Callback redirects with ?code=<temp_code>, not the JWT itself.
        Trade it in here for the real access_token."""
        result = self._post(EP_EXCHANGE, {"code": code})
        token = result.get("access_token")
        if token:
            self.set_token(token)
        return result

    def logout(self):
        try:
            result = self._get(EP_LOGOUT)
        finally:
            self.clear_token()
        return result

    def get_me(self):
        return self._get(EP_ME)

    # ---------- upload ----------
    def upload_document(self, file_name: str, file_bytes: bytes, content_type: str):
        try:
            resp = self.session.post(
                f"{API_BASE_URL}{EP_UPLOAD}",
                files={"file": (file_name, file_bytes, content_type)},
                timeout=REQUEST_TIMEOUT,
            )
        except requests.RequestException as e:
            raise APIError(f"Could not reach backend: {e}")
        return self._handle(resp)

    # ---------- chat ----------
    def chat(self, document_id: str, question: str):
        return self._post(EP_CHAT, {"document_id": document_id, "question": question})

    # ---------- summary ----------
    def summary(self, document_id: str, topic: str):
        return self._post(EP_SUMMARY, {"document_id": document_id, "topic": topic})

    # ---------- notes ----------
    def notes(self, document_id: str, topic: str):
        return self._post(EP_NOTES, {"document_id": document_id, "topic": topic})

    # ---------- quiz ----------
    def quiz(self, document_id: str, topic: str, difficulty: str, number_of_questions: int):
        return self._post(EP_QUIZ, {
            "document_id": document_id,
            "topic": topic,
            "difficulty": difficulty,
            "number_of_questions": number_of_questions,
        })

    def submit_quiz(self, quiz_id: str, answers: list[dict]):
        return self._post(f"{EP_QUIZ}submit", {
            "quiz_id": quiz_id,
            "answers": answers,
        })


    # ---------- internals ----------
    def _get(self, path):
        try:
            resp = self.session.get(f"{API_BASE_URL}{path}", timeout=REQUEST_TIMEOUT)
        except requests.RequestException as e:
            raise APIError(f"Could not reach backend: {e}")
        return self._handle(resp)

    def _post(self, path, payload):
        try:
            resp = self.session.post(f"{API_BASE_URL}{path}", json=payload, timeout=REQUEST_TIMEOUT)
        except requests.RequestException as e:
            raise APIError(f"Could not reach backend: {e}")
        return self._handle(resp)

    @staticmethod
    def _handle(resp: requests.Response):
        if resp.status_code >= 400:
            detail = resp.text
            try:
                detail = resp.json().get("detail", detail)
            except Exception:
                pass
            raise APIError(detail, status_code=resp.status_code)
        try:
            return resp.json()
        except ValueError:
            return {}
