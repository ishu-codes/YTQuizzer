import streamlit as st
import jsonification
import prompt
import summariser
import transcriptor
from openai import RateLimitError

class Home:
    def __init__(self) -> None:
        pass

    def load(self):
        with st.container():
            st.markdown("""### Enter the YouTube URL""")
            link = st.text_input("", placeholder="Paste the link here")

            if st.button("Get Summary"):
                try:
                    with st.spinner("Brewing your Summary and Quiz!"):
                        t = transcriptor.get_transcript(link)
                        summariser.get_summary(t)
                        with open("quiz.json", "w") as json_file:
                            json_file.write('')
                        jsonification.lists_of_lists_to_json(prompt.get_quiz(t), 'quiz.json')
                        pressed = True
                    st.write("please go to the summary and quiz page to view the generated summary and quiz respectively.")
                except RateLimitError as error:
                    st.error(error.body['message'])

def main():
    page = Home()

if __name__ == "__main__":
    main()
