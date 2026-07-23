from fastapi import APIRouter


router = APIRouter(
    prefix="/summary",
    tags=["Summary"]
)


@router.post("/")
def summary():
    return {
        "message": "Summary endpoint"
    }