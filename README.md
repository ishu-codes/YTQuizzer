# Quizify

# Project Report: Quizify - A Python-Based Learning Tool

## Introduction:

Quizify is an innovative Python-based project designed to enhance the learning experience by generating video summaries, interactive quizzes, and incorporating a chatbot for doubt clarification.

---

## Functionalities:

### Video Summarization:

> -   _Youtube_transcript_api:_ This library will be crucial for extracting transcripts from YouTube videos, providing the textual basis for summarization.
> -   _Google Gemini 1.0 Pro:_ This library takes the input of YouTube video transcript, and then generating summary of the video along with quiz questions and options.
> -   _OpenAI ChatGPT 3.5 Turbo:_ These library is providing responses to the queries asked by the user in the Chatbot section.

### Interactive Quizzes:

> -   **Streamlit:** This framework will serve as the foundation for building the user interface, allowing users to interact with the quizzes and view their results.

### Chatbot Integration:

> -   _Openai:_ OpenAI's language models can power a sophisticated chatbot capable of understanding and responding to user queries related to the video content.
> -   _Streamlit:_ The chatbot interface can be seamlessly integrated into the Streamlit application, providing a user-friendly experience.

## Benefits:

> -   **Efficient Learning:** Quizify optimizes the learning process by providing concise summaries, interactive assessments, and immediate doubt resolution.
> -   **Enhanced Understanding:** The combination of summaries, quizzes, and chatbot support ensures comprehensive understanding and knowledge retention.
> -   **Personalized Learning:** Feedback and recommendations are tailored to individual needs, identifying areas for improvement and promoting targeted learning.
> -   **Engaging Experience:** Gamification elements and interactive features make learning enjoyable and motivating.
> -   **Active Recall** After revision the interactive quizzes can be used to facilitate active recall to enable deeper understanding of the underlying concepts

## Project Architecture:

![Data flow](./assets/Data_flow.png)

### Frontend:

> -   **Streamlit:** Serves as the primary framework for building the user interface, including video input, summary display, quiz interactions, and chatbot integration.
> -   **Streamlit-option-menu:** Enhances the user interface with a navigation menu, allowing users to easily switch between different functionalities.
> -   **Streamlit-shadcn-ui:** Provides additional UI components and styling options to create a visually appealing and user-friendly experience.

### Backend:

> -   _Youtube Transcript API:_ Handles the extraction of transcripts from YouTube videos.
> -   _Google generative AI or openai:_ Provides the language models for generating video summaries and powering the chatbot's responses.
> -   _Pandas:_ Assists in data organization and analysis for quiz generation.

### Implementation Workflow:

> -   **Video Input:** Users input the YouTube video URL through a Streamlit interface.
> -   **Transcript Extraction:** The youtube_transcript_api library fetches and processes the video transcript.
> -   **Summarization:** The extracted transcript is passed to either google-generative ai to generate a concise summary.
> -   **Quiz Generation:** Python standard libraries like json are used to handle data processing
> -   **Chatbot Integration:** OpenAi's language models are employed to build a chatbot capable of answering user questions related to the video content.
> -   **User Interface:** Streamlit, along with streamlit-option-menu and streamlit-shadcn-ui, creates a user-friendly interface for accessing summaries, taking quizzes, and interacting with the chatbot.

## Conclusion:
> By leveraging the power of Streamlit and other chosen tools, Quizify offers a robust and engaging learning platform. Its ability to summarize videos, generate quizzes, and provide chatbot assistance personalizes and enhances the learning experience, making it a valuable tool for a wide range of users.

## Checkout the live working

https://quizify.streamlit.app/
