from fastapi import APIRouter


router = APIRouter(
    prefix="/quiz",
    tags=["Quiz"]
)


@router.post("/")
def quiz():
    return {
        "message": "Quiz endpoint"
    }