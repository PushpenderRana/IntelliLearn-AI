from fastapi import APIRouter

from app.api.routes.upload import router as upload_router
from app.api.routes.chat import router as chat_router
from app.api.routes.summary import router as summary_router
from app.api.routes.notes import router as notes_router
from app.api.routes.quiz import router as quiz_router
from app.api.routes.auth import router as auth_router


api_router = APIRouter()

api_router.include_router(upload_router)
api_router.include_router(chat_router)
api_router.include_router(summary_router)
api_router.include_router(notes_router)
api_router.include_router(quiz_router)
api_router.include_router(auth_router)