from fastapi import APIRouter, HTTPException

from app.schemas.notes import NotesRequest, NotesResponse
from app.services.ai.notes import NotesService
from app.services.rag.manager import rag_pipeline


router = APIRouter(
    prefix="/notes",
    tags=["Notes"]
)


@router.post("/", response_model=NotesResponse)
async def notes(request: NotesRequest):
    if request.document_id not in rag_pipeline.retrievers:
        raise HTTPException(
        status_code=400,
        detail="Document not indexed."
    )

    notes_service = NotesService(rag_pipeline)

    result = notes_service.generate_notes(request.document_id,request.topic)

    return NotesResponse(notes=result)