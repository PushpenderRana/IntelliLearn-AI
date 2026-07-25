import os
from pathlib import Path
from dotenv import load_dotenv

env_path = Path(__file__).resolve().parents[2] / ".env"
load_dotenv(dotenv_path=env_path)

class Settings:
    PRIMARY_MODEL: str = os.getenv("PRIMARY_MODEL") or "minimax-m3:cloud"
    FALLBACK_MODEL: str = os.getenv("FALLBACK_MODEL") or "nemotron-3-super:cloud"
    EMBEDDING_MODEL: str = os.getenv("EMBEDDING_MODEL") or "nomic-embed-text"
    GOOGLE_CLIENT_ID: str = os.getenv("GOOGLE_CLIENT_ID", "")
    GOOGLE_CLIENT_SECRET: str = os.getenv("GOOGLE_CLIENT_SECRET", "")
    SESSION_SECRET: str = os.getenv("SESSION_SECRET", "default_secret_key_change_me")
    OLLAMA_API_KEY: str = os.getenv("OLLAMA_API_KEY", "")
    GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
    OLLAMA_BASE_URL: str = os.getenv("OLLAMA_BASE_URL", "https://ollama.com")


settings = Settings()


