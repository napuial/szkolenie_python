import streamlit as st
import json

if "quiz" not in st.session_state:
    st.session_state.quiz = []
if "loaded_quiz" not in st.session_state:
    st.session_state.loaded_quiz = []

def add_question():
    if len(st.session_state.quiz) >= 3:
        st.warning("Quiz może zawierać maksymalnie 3 pytania!")
        return
    if st.session_state.pytanie_input and st.session_state.odp1_input and st.session_state.odp2_input and st.session_state.odp3_input:
        st.session_state.quiz.append({
            "question": st.session_state.pytanie_input,
            "answers": [
                st.session_state.odp1_input,
                st.session_state.odp2_input,
                st.session_state.odp3_input
            ],
            "correct": int(st.session_state.poprawna_input) - 1
        })
        st.session_state.pytanie_input = ""
        st.session_state.odp1_input = ""
        st.session_state.odp2_input = ""
        st.session_state.odp3_input = ""
        st.session_state.poprawna_input = "1"
        st.success("Pytanie dodane!")
    else:
        st.error("Uzupełnij wszystkie pola!")

st.subheader("Wczytaj quiz z pliku JSON")
uploaded_file = st.file_uploader("Wybierz plik JSON", type="json")
if uploaded_file:
    st.session_state.loaded_quiz = json.load(uploaded_file)
    st.session_state.quiz = st.session_state.loaded_quiz.copy()
    st.success("Quiz wczytany!")

st.subheader("Dodaj pytanie")
with st.form("quiz_form", clear_on_submit=False):
    pytanie = st.text_input("Treść pytania", key="pytanie_input")
    odp1 = st.text_input("Odpowiedź 1", key="odp1_input")
    odp2 = st.text_input("Odpowiedź 2", key="odp2_input")
    odp3 = st.text_input("Odpowiedź 3", key="odp3_input")
    poprawna = st.radio("Która odpowiedź jest poprawna?", ["1", "2", "3"], index=0, key="poprawna_input")
    st.form_submit_button("Dodaj pytanie", on_click=add_question)

if st.session_state.quiz:
    st.subheader("Aktualne pytania w quizie")
    for i, q in enumerate(st.session_state.quiz, start=1):
        st.write(f"{i}. {q['question']}")
        for j, a in enumerate(q['answers']):
            st.markdown(f"<span style='margin-left: 20px;'>{chr(ord('a') + j)}) {a} {'✅' if j == q['correct'] else ''}</span>",
            unsafe_allow_html=True)

if st.session_state.quiz:
    st.subheader("Pobierz quiz jako JSON")
    quiz_json = json.dumps(st.session_state.quiz, ensure_ascii=False, indent=4)
    st.download_button("Pobierz quiz", quiz_json, file_name="quiz.json", mime="application/json")
