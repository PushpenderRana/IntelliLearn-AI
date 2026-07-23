from fastapi import FastAPI

from app.api.router import api_router


app = FastAPI(
    title="IntelliLearn AI",
    version="1.0.0",
    description="RAG-Based Personalized Learning Platform"
)

app.include_router(api_router)


@app.get("/")
def root():
    return {
        "message": "Welcome to IntelliLearn AI API"
    }