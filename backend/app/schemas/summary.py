from pydantic import BaseModel


class SummaryRequest(BaseModel):
    document_id: str
    topic: str


class SummaryResponse(BaseModel):
    summary: str