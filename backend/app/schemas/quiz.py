from typing import Any, Optional
from pydantic import BaseModel


class QuizRequest(BaseModel):
    document_id: str
    topic: str
    difficulty: str = "medium"
    number_of_questions: int = 5


class QuizQuestionItem(BaseModel):
    question_id: int
    question: str
    options: dict[str, str]
    difficulty: str


class QuizResponse(BaseModel):
    quiz_id: str
    questions: list[QuizQuestionItem]


class QuizAnswerItem(BaseModel):
    question_id: int
    selected: str


class QuizSubmitRequest(BaseModel):
    quiz_id: str
    answers: list[QuizAnswerItem]


class QuizResultDetail(BaseModel):
    question_id: int
    question: str
    selected_answer: Optional[str] = None
    correct_answer: str
    is_correct: bool
    explanation: Optional[str] = ""


class QuizSubmitResponse(BaseModel):
    score: int
    total: int
    percentage: float
    correct: int
    wrong: int
    unanswered: int
    passed: bool
    results: list[QuizResultDetail]