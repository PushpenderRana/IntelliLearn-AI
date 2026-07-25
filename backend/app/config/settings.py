import os
from pathlib import Path
from dotenv import load_dotenv

env_path = Path(__file__).resolve().parents[2] / ".env"
load_dotenv(dotenv_path=env_path)


class Settings:
    # LLM
    PRIMARY_MODEL: str = os.getenv("PRIMARY_MODEL", "llama-3.3-70b-versatile")
    FALLBACK_MODEL: str = os.getenv("FALLBACK_MODEL", "llama-3.1-8b-instant")
    GROQ_API_KEY: str = os.getenv("GROQ_API_KEY", "")

    # Embeddings
    GOOGLE_API_KEY: str = os.getenv("GOOGLE_API_KEY", "")
    EMBEDDING_MODEL: str = os.getenv(
        "EMBEDDING_MODEL",
        "models/gemini-embedding-001"
    )

    # Google OAuth
    GOOGLE_CLIENT_ID: str = os.getenv("GOOGLE_CLIENT_ID", "")
    GOOGLE_CLIENT_SECRET: str = os.getenv("GOOGLE_CLIENT_SECRET", "")

    # Session
    SESSION_SECRET: str = os.getenv(
        "SESSION_SECRET",
        "default_secret_key_change_me"
    )


settings = Settings()