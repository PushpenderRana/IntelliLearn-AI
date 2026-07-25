from app.services.ai.cache_service import cache_service


class QuizNotFoundError(Exception):
    pass


def evaluate_quiz(quiz_id: str, answers: list[dict], pass_threshold: float = 50.0) -> dict:
    cached = cache_service.get(quiz_id)
    if cached is None:
        raise QuizNotFoundError(f"Quiz {quiz_id} not found or expired")

    questions = cached["questions"]
    answer_map = {a["question_id"]: str(a.get("selected", "")).strip().upper()[:1] for a in answers}

    results = []
    correct = wrong = unanswered = 0

    for q in questions:
        qid = q["question_id"]
        selected = answer_map.get(qid)
        correct_answer = q["answer"]

        if not selected:
            unanswered += 1
            is_correct = False
        else:
            is_correct = selected == correct_answer
            correct += 1 if is_correct else 0
            wrong += 0 if is_correct else 1

        results.append({
            "question_id": qid,
            "question": q["question"],
            "selected_answer": selected,
            "correct_answer": correct_answer,
            "is_correct": is_correct,
            "explanation": q.get("explanation", ""),
        })

    total = len(questions)
    percentage = round((correct / total) * 100, 2) if total else 0.0

    # One-shot: cache gone after grading, re-submit impossible, no answer-tweak replay.
    cache_service.delete(quiz_id)

    return {
        "score": correct,
        "total": total,
        "percentage": percentage,
        "correct": correct,
        "wrong": wrong,
        "unanswered": unanswered,
        "passed": percentage >= pass_threshold,
        "results": results,
    }