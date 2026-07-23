from fastapi import APIRouter


router = APIRouter(
    prefix="/flashcards",
    tags=["Flashcards"]
)


@router.post("/")
def flashcards():
    return {
        "message": "Flashcards endpoint"
    }