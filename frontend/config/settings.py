"""
Central config. Change API_BASE_URL to point at your running FastAPI backend.
"""
import os

API_BASE_URL = os.getenv("INTELLILEARN_API_URL", "https://intellilearn-ai-8r6m.onrender.com")

APP_NAME = "IntelliLearn AI"
APP_TAGLINE = "Learn Smarter with AI-Powered Personalized Learning"

# Endpoints — must match backend exactly, do not invent new ones.
EP_LOGIN = "/auth/login"
EP_CALLBACK = "/auth/callback"
EP_EXCHANGE = "/auth/exchange"
EP_LOGOUT = "/auth/logout"
EP_ME = "/auth/me"
EP_UPLOAD = "/upload/"
EP_CHAT = "/chat/"
EP_SUMMARY = "/summary/"
EP_NOTES = "/notes/"
EP_QUIZ = "/quiz/"


REQUEST_TIMEOUT = 60

# Theme
THEME_COLORS = {
    "dark": {
        "bg": "#0f0f1a",
        "bg_secondary": "#161625",
        "glass": "rgba(255, 255, 255, 0.06)",
        "glass_border": "rgba(255, 255, 255, 0.12)",
        "text": "#f1f1f8",
        "text_muted": "#9a9ab0",
        "gradient_start": "#7c3aed",
        "gradient_end": "#06b6d4",
        "accent": "#a78bfa",
        "success": "#34d399",
        "error": "#f87171",
    },
    "light": {
        "bg": "#f6f7fb",
        "bg_secondary": "#ffffff",
        "glass": "rgba(255, 255, 255, 0.65)",
        "glass_border": "rgba(15, 15, 26, 0.08)",
        "text": "#181825",
        "text_muted": "#6b6b80",
        "gradient_start": "#7c3aed",
        "gradient_end": "#06b6d4",
        "accent": "#7c3aed",
        "success": "#059669",
        "error": "#dc2626",
    },
}
