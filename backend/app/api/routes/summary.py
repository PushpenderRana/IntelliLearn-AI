from fastapi import APIRouter, HTTPException

from app.schemas.summary import SummaryRequest, SummaryResponse
from app.services.ai.summary import SummaryService
from app.services.rag.manager import rag_pipeline


router = APIRouter(
    prefix="/summary",
    tags=["Summary"]
)


@router.post("/", response_model=SummaryResponse)
async def summary(request: SummaryRequest):
    if request.document_id not in rag_pipeline.retrievers:
        raise HTTPException(
        status_code=400,
        detail="Document not indexed."
    )

    summary_service = SummaryService(rag_pipeline)

    result = summary_service.generate_summary(request.document_id,request.topic)

    return SummaryResponse(summary=result)