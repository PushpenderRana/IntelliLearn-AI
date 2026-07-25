from pathlib import Path
import shutil
import uuid

from app.schemas.upload import UploadResponse
from app.services.rag.manager import rag_pipeline

from app.auth.dependencies import get_current_user
from typing import Annotated

from fastapi import APIRouter, Depends, File, HTTPException, UploadFile


router = APIRouter(
    prefix="/upload",
    tags=["Upload"]
)

UPLOAD_DIR = Path("app/uploads")
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)


@router.post("/", response_model=UploadResponse)
async def upload_document(
    file: UploadFile = File(...),
    user: Annotated[dict, Depends(get_current_user)] = None
):
    if not file.filename:
        raise HTTPException(
        status_code=400,
        detail="No file selected."
    )
    extension = Path(file.filename).suffix.lower()

    if extension not in [".pdf", ".docx"]:
        raise HTTPException(
            status_code=400,
            detail="Only PDF and DOCX files are supported."
        )

    file_path = UPLOAD_DIR / file.filename

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    document_id = str(uuid.uuid4())
    rag_pipeline.index_document(
        document_id=document_id,
        file_path=str(file_path))

    return UploadResponse(
        message="Document uploaded and indexed successfully.",
        filename=file.filename,
        document_id=document_id
    )