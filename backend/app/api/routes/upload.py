from pathlib import Path
import shutil

from fastapi import APIRouter, File, HTTPException, UploadFile

from app.schemas.upload import UploadResponse
from app.services.rag.pipeline import RAGPipeline


router = APIRouter(
    prefix="/upload",
    tags=["Upload"]
)

UPLOAD_DIR = Path("app/uploads")
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)

rag = RAGPipeline()


@router.post("/", response_model=UploadResponse)
async def upload_document(file: UploadFile = File(...)):
    if file.filename is None:
        raise HTTPException(
            status_code=400,
            detail="No file uploaded."
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

    rag.index_document(str(file_path))

    return UploadResponse(
        message="Document uploaded and indexed successfully.",
        filename=file.filename
    )