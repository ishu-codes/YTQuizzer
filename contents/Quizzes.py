import streamlit as st
from json import loads, JSONDecodeError
import random

class Quizzes:
    def __init__(self) -> None:
        pass

    def load(self):
        with st.container():
            with open('quiz.json', 'r') as file:
                file_content = file.read()
            
            try:
                questions = loads(file_content)
            except JSONDecodeError:
                st.warning('Quizzes cannot be generated!', icon="⚠️")
                st.text("Make sure that you pasted the YouTube URL correctly!")
                return

            st.title("Quiz Time!")
            score = 0
            correct_answers = 0

            # Initialize quiz_answers if not already set
            if 'quiz_answers' not in st.session_state:
                st.session_state.quiz_answers = {i: None for i in range(len(questions))}

            # Initialize shuffled_options if not already set
            if 'shuffled_options' not in st.session_state:
                st.session_state.shuffled_options = {}
                for i, question in enumerate(questions):
                    options = [question['answer'], question['wrong_answer1'], question['wrong_answer2']]
                    random.shuffle(options)
                    st.session_state.shuffled_options[i] = options

            # Display each question and get user input
            for i, question in enumerate(questions, 1):  # Start index at 1 for display
                st.subheader(f"Question {i}: {question['question']}")

                # Get previously selected answer (if any)
                selected_option = st.session_state.quiz_answers.get(i - 1, None)  # Use i-1 to match dictionary index

                # Use the stored shuffled options
                options = st.session_state.shuffled_options[i - 1]

                # Check if selected_option is in the options list before trying to find its index
                if selected_option is not None and selected_option in options:
                    selected_index = options.index(selected_option)
                else:
                    # Set a default index or handle the situation differently
                    selected_index = 0  # or any other default index

                # Always render the radio button widget and set the state unconditionally
                selected_option = st.radio("Choose an option", options, key=f"question_{i}", index=selected_index)
                # Update answers dictionary
                st.session_state.quiz_answers[i - 1] = selected_option  # Use i-1 to match dictionary index

            # Calculate score correctly using i-1 to match dictionary index
            for i, question in enumerate(questions, 1):
                if st.session_state.quiz_answers.get(i - 1) == question['answer']:
                    correct_answers += 1

            # Display the score
            score = correct_answers
            st.write(f"Your final score is: {score}/{len(questions)}")

def main():
    page = Quizzes()

if __name__ == "__main__":
    main()