from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware.sessions import SessionMiddleware

from app.api.router import api_router
from app.config.settings import settings

app = FastAPI(
    title="IntelliLearn AI",
    version="1.0.0",
    description="RAG-Based Personalized Learning Platform"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.add_middleware(
    SessionMiddleware,
    secret_key=settings.SESSION_SECRET
)

app.include_router(api_router)



@app.get("/")
def root():
    return {
        "message": "Welcome to IntelliLearn AI API"
    }