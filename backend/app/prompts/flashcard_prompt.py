FLASHCARD_PROMPT = """
You are an expert teacher.

Using only the context below, generate study flashcards.

Instructions:
- Create question-answer flashcards.
- Keep each answer concise.
- Cover all important concepts.
- Do not use information outside the provided context.

Context:
{context}

Topic:
{query}

Flashcards:
"""