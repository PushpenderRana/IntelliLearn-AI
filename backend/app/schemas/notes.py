from pydantic import BaseModel


class NotesRequest(BaseModel):
    document_id: str
    topic: str


class NotesResponse(BaseModel):
    notes: str