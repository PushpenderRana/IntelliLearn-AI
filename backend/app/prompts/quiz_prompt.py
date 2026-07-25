QUIZ_PROMPT = """
You are an expert teacher.

Using ONLY the context below, generate a multiple-choice quiz.

Instructions:
- Difficulty: {difficulty}
- Number of Questions: {number_of_questions}
- Each question must have exactly four options (A, B, C, D).
- Provide the correct answer after each question.
- Do not use information outside the provided context.

Context:
{context}

Topic:
{query}

Quiz:
"""