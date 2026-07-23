import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    PRIMARY_MODEL = os.getenv("PRIMARY_MODEL")
    FALLBACK_MODEL = os.getenv("FALLBACK_MODEL")
    EMBEDDING_MODEL = os.getenv("EMBEDDING_MODEL")


settings = Settings()