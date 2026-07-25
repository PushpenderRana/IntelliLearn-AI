from fastapi import APIRouter, HTTPException

from app.schemas.chat import ChatRequest, ChatResponse
from app.services.ai.chat import ChatService
from app.services.rag.manager import rag_pipeline


router = APIRouter(
    prefix="/chat",
    tags=["Chat"]
)


@router.post("/", response_model=ChatResponse)
async def chat(request: ChatRequest):
    if request.document_id not in rag_pipeline.retrievers:
        raise HTTPException(
        status_code=400,
        detail="Document not indexed."
    )

    chat_service = ChatService(rag_pipeline)

    answer = chat_service.ask(request.document_id,request.question)

    return ChatResponse(answer=answer)