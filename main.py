import streamlit as st
from streamlit_option_menu import option_menu

from contents.Home import Home
from contents.Summary import Summary
from contents.Quizzes import Quizzes
from contents.Chatbot import Chatbot
from contents.ErrorPage import ErrorPage

class App:
    __NAVBAR = {'Home':0, 'Summary':1, 'Quizzes':2, 'Chatbot':3}
    __NAVBAR_ICONS = ['house', 'book', 'code-slash', 'robot']

    def __init__(self) -> None:
        pass

    def load(self):
        st.set_page_config(
            page_title="Quizzify",
            page_icon="https://raw.githubusercontent.com/github/explore/968d1eb8fb6b704c6be917f0000283face4f33ee/topics/streamlit/streamlit.png",
            layout="centered",
            initial_sidebar_state="collapsed",
        )

        # Navbar
        with st.container():
            navbar = option_menu(
                menu_title=None,
                options=list(self.__NAVBAR.keys()),
                icons=self.__NAVBAR_ICONS,
                orientation='horizontal',
                default_index=self.__NAVBAR.get(st.session_state.get("navbar", 'Home'))
            )
        page = ErrorPage()
        match(navbar):
            case "Home": page = Home()
            case "Summary": page = Summary()
            case "Quizzes": page = Quizzes()
            case "Chatbot": page = Chatbot()
                
        page.load()

def main():
    app = App()
    app.load()

if __name__ == "__main__":
    main()
