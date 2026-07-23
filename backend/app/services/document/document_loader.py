from pathlib import Path

from app.services.document.pdf_loader import load_pdf
from app.services.document.docx_loader import load_docx


def load_document(file_path: str):
    extension = Path(file_path).suffix.lower()

    if extension == ".pdf":
        return load_pdf(file_path)

    if extension == ".docx":
        return load_docx(file_path)

    raise ValueError(f"Unsupported file type: {extension}")