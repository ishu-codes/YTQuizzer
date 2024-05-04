import streamlit as st
from openai import OpenAI, RateLimitError
from os import environ

class Chatbot:
    def __init__(self) -> None:
        pass

    def load(self):
        environ["OPENAI_API_KEY"] = st.secrets.openAi_api.key
        client = OpenAI()

        st.session_state.setdefault("model", "gpt-3.5-turbo")
        st.session_state.setdefault("messages", [{"role": "assistant", "content": "How can I help you today?"}])

        with st.container():
            st.markdown("""<style>div.stChatInput { position:fixed; bottom:1rem; z-index:10; }</style>""", unsafe_allow_html=True
            )
            for message in st.session_state.messages:
                with st.chat_message(message["role"]):
                    st.markdown(message["content"])


            if prompt := st.chat_input("Message ChatGPT"):
                st.session_state.messages.append({"role": "user", "content": prompt})
                with st.chat_message("user"):
                    st.markdown(prompt)

                with st.chat_message("assistant"):
                    stream = None
                    try:
                        stream = client.chat.completions.create(
                            model=st.session_state["model"],
                            messages=[
                                {"role": message["role"], "content": message["content"]}
                                for message in st.session_state.messages
                            ],
                            stream=True,
                        )
                        response = st.write_stream(stream)
                        st.session_state.messages.append({"role": "assistant", "content": response})

                    except RateLimitError as error:
                        st.info(error.body['message'])
                        st.session_state.messages.append({"role": "assistant", "content": error.body['message']})


def main():
    page = Chatbot()

if __name__ == "__main__":
    main()