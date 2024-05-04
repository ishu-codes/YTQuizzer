import streamlit as st

class ErrorPage:
    def __init__(self) -> None:
        pass

    def load(self):
        with st.container:
            st.title("ErrorPage")

def main():
    page = ErrorPage()

if __name__ == "__main__":
    main()