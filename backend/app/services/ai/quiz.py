import json
import re
from app.prompts.quiz_prompt import QUIZ_PROMPT
from app.services.rag.base_service import BaseRAGService
from app.services.ai.cache_service import cache_service


class QuizService(BaseRAGService):
    def generate_quiz(self, document_id: str, topic: str, difficulty: str = "medium", number_of_questions: int = 5) -> dict:
        prompt_with_json_instruction = (
            QUIZ_PROMPT + "\n\nFormat your output as a JSON array of objects with keys: "
            '"question", "options" (array of 4 strings), "answer" (single letter A/B/C/D), "explanation".'
        )
        
        raw_output = self.generate(
            document_id=document_id,
            query=topic,
            prompt_template=prompt_with_json_instruction,
            difficulty=difficulty,
            number_of_questions=number_of_questions
        )
        
        parsed_questions = _parse_llm_quiz_response(raw_output, difficulty, number_of_questions)

        full_questions = []
        for i, q in enumerate(parsed_questions, start=1):
            opts = q.get("options", [])
            if isinstance(opts, list):
                letters = ["A", "B", "C", "D"][:len(opts)]
                options_dict = dict(zip(letters, opts))
            elif isinstance(opts, dict):
                options_dict = opts
            else:
                options_dict = {"A": "Option A", "B": "Option B", "C": "Option C", "D": "Option D"}

            full_questions.append({
                "question_id": i,
                "question": q.get("question", f"Question {i}"),
                "options": options_dict,
                "answer": str(q.get("answer", "A")).strip().upper()[:1],
                "explanation": q.get("explanation", ""),
                "difficulty": difficulty,
            })

        quiz_id = cache_service.create({
            "document_id": document_id,
            "topic": topic,
            "difficulty": difficulty,
            "questions": full_questions,
        })

        public_questions = [
            {
                "question_id": q["question_id"],
                "question": q["question"],
                "options": q["options"],
                "difficulty": q["difficulty"],
            }
            for q in full_questions
        ]

        return {"quiz_id": quiz_id, "questions": public_questions}


def _parse_llm_quiz_response(text: str, difficulty: str, n_questions: int) -> list[dict]:
    if not text:
        return []
    
    json_match = re.search(r'\[.*\]', text, re.DOTALL)
    if json_match:
        try:
            return json.loads(json_match.group(0))
        except Exception:
            pass

    try:
        data = json.loads(text)
        if isinstance(data, list):
            return data
        if isinstance(data, dict) and "questions" in data:
            return data["questions"]
    except Exception:
        pass

    questions = []
    blocks = re.split(r'\n(?=Q\d+|\d+[\.\)])', text)
    for b in blocks:
        lines = [line.strip() for line in b.split('\n') if line.strip()]
        if not lines:
            continue
        q_text = lines[0]
        options = []
        answer = "A"
        explanation = ""
        for line in lines[1:]:
            if re.match(r'^[A-D][\.\)]', line, re.IGNORECASE):
                options.append(line[2:].strip())
            elif "answer:" in line.lower():
                m = re.search(r'[A-D]', line, re.IGNORECASE)
                if m:
                    answer = m.group(0).upper()
            elif "explanation:" in line.lower():
                explanation = line.split(":", 1)[-1].strip()

        if len(options) < 2:
            options = ["Option A", "Option B", "Option C", "Option D"]

        questions.append({
            "question": q_text,
            "options": options,
            "answer": answer,
            "explanation": explanation
        })

    return questions