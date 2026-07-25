from fastapi import APIRouter, HTTPException

from app.schemas.quiz import (
    QuizRequest, QuizResponse, QuizSubmitRequest, QuizSubmitResponse
)
from app.services.ai.quiz import QuizService
from app.services.ai.evaluation import evaluate_quiz, QuizNotFoundError
from app.services.rag.manager import rag_pipeline


router = APIRouter(
    prefix="/quiz",
    tags=["Quiz"]
)


@router.post("/", response_model=QuizResponse)
async def quiz(request: QuizRequest):
    if request.document_id not in rag_pipeline.retrievers:
        raise HTTPException(
            status_code=400,
            detail="Document not indexed."
        )

    quiz_service = QuizService(rag_pipeline)

    result = quiz_service.generate_quiz(
        document_id=request.document_id,
        topic=request.topic,
        difficulty=request.difficulty,
        number_of_questions=request.number_of_questions
    )

    return QuizResponse(**result)


@router.post("/submit", response_model=QuizSubmitResponse)
async def submit_quiz(request: QuizSubmitRequest):
    try:
        answers = [a.model_dump() for a in request.answers]
        result = evaluate_quiz(quiz_id=request.quiz_id, answers=answers)
        return QuizSubmitResponse(**result)
    except QuizNotFoundError as e:
        raise HTTPException(
            status_code=404,
            detail=str(e)
        )
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Evaluation failed: {str(e)}"
        )