import streamlit as st

class Summary:
    def __init__(self) -> None:
        pass

    def load(self):
        with st.container():
            file_content = ''
            with open('sum.txt', 'r') as file:
                file_content = file.read()
            
            if not file_content.strip():
                st.warning('Summary cannot be generated!', icon="⚠️")
                st.text("Make sure that you pasted the YouTube URL correctly!")
                return

            st.markdown("# Summary of the video:")

            # a = summariser.get_summary(transcriptor.get_transcript(link))
            # st.write(a)

            # Read the content of the summary.txt file
            with open("sum.txt", "r") as f:
                summary_text = f.read()
            st.write(summary_text)
            with open("sum.txt", "w") as f:
                f.write("")
            st.write("")

def main():
    page = Summary()

if __name__ == "__main__":
    main()
