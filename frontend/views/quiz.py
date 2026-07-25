import streamlit as st
from utils.session import api, bump_stat
from services.api import APIError
from components.ui import section_header, error_banner


def render():
    section_header("❓ AI Quiz", "Test yourself with auto-generated MCQs.")

    if not st.session_state.document_id:
        st.warning("Upload a document first from **Upload Document**.")
        return

    with st.container():
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        topic = st.text_input("Topic", placeholder="e.g. entire document, chapter 1...")
        c1, c2 = st.columns(2)
        difficulty = c1.selectbox("Difficulty", ["Easy", "Medium", "Hard"])
        n_questions = c2.number_input("Number of Questions", min_value=1, max_value=20, value=5)

        if st.button("🎯  Generate Quiz", use_container_width=True):
            with st.spinner("Generating quiz..."):
                try:
                    result = api().quiz(st.session_state.document_id, topic or "entire document",
                                        difficulty.lower(), int(n_questions))
                    st.session_state.quiz_id = result.get("quiz_id")
                    st.session_state.quiz_data = result.get("questions", [])
                    st.session_state.quiz_index = 0
                    st.session_state.quiz_selected = {}
                    st.session_state.quiz_result = None
                    bump_stat("quizzes_generated")
                except APIError as e:
                    error_banner(f"Quiz generation failed: {e.message}")
        st.markdown('</div>', unsafe_allow_html=True)

    result = st.session_state.get("quiz_result")
    if result:
        _render_results(result)
        return

    quiz = st.session_state.get("quiz_data")
    if not quiz:
        return

    idx = st.session_state.quiz_index
    total = len(quiz)
    q = quiz[idx]
    qid = q["question_id"]

    st.markdown(
        f'<div class="glass-card"><b>Question {idx + 1} of {total}</b> · {q.get("difficulty", "")}'
        f'<br><br>{q.get("question", "")}</div>',
        unsafe_allow_html=True,
    )

    options = q.get("options", {})
    keys = list(options.keys())
    default = st.session_state.quiz_selected.get(qid)
    choice = st.radio(
        "Choose an answer", keys,
        index=keys.index(default) if default in keys else 0,
        format_func=lambda k: f"{k}. {options[k]}", key=f"quiz_choice_{qid}",
    )
    st.session_state.quiz_selected[qid] = choice

    c1, c2 = st.columns(2)
    if idx > 0 and c1.button("⬅  Previous", use_container_width=True):
        st.session_state.quiz_index -= 1
        st.rerun()

    is_last = idx == total - 1
    label = "✅  Submit Quiz" if is_last else "Next Question ➡"
    if c2.button(label, use_container_width=True):
        if is_last:
            _submit_quiz()
        else:
            st.session_state.quiz_index += 1
            st.rerun()


def _submit_quiz():
    answers = [{"question_id": qid, "selected": ans} for qid, ans in st.session_state.quiz_selected.items()]
    with st.spinner("Grading quiz..."):
        try:
            result = api().submit_quiz(st.session_state.quiz_id, answers)
            st.session_state.quiz_result = result
            bump_stat("quizzes_completed")
        except APIError as e:
            error_banner(f"Submission failed: {e.message}")
            return
    st.rerun()


def _render_results(result):
    status = ("✅ Passed" if result.get("passed") else "❌ Failed") if "passed" in result else ""
    st.markdown(f"""
    <div class="glass-card" style="text-align:center;">
        <h3>🏁 Quiz Complete! {status}</h3>
        <div class="stat-value">{result['score']} / {result['total']}</div>
        <p>{result['percentage']}% · {result['correct']} correct · {result['wrong']} wrong · {result['unanswered']} unanswered</p>
    </div>
    """, unsafe_allow_html=True)

    for i, r in enumerate(result.get("results", []), start=1):
        mark = "✅" if r["is_correct"] else "❌"
        st.markdown(f"""
        <div class="glass-card">
            <b>{mark} Q{i}. {r['question']}</b><br>
            Your answer: <b>{r['selected_answer'] or '—'}</b> &nbsp;|&nbsp; Correct answer: <b>{r['correct_answer']}</b>
            {f"<br><i>{r['explanation']}</i>" if r.get('explanation') else ''}
        </div>
        """, unsafe_allow_html=True)

    if st.button("🔁  Retake Quiz", use_container_width=True):
        for k in ("quiz_data", "quiz_id", "quiz_selected", "quiz_result"):
            st.session_state[k] = None
        st.session_state.quiz_index = 0
        st.rerun()