# ai_doctor

# AI Doctor Chatbot

This is an AI-powered doctor chatbot built using **Streamlit** and **LangChain**. The chatbot is designed to answer medical-related questions and provide short, precise responses. It uses speech recognition to allow users to ask questions via voice. The model used for answering the questions is powered by **Groq** and **LangChain**.

## Features
- **Voice Input**: Users can speak their questions, and the chatbot will recognize the speech using the Google Speech API.
- **Medical Expertise**: The chatbot is specialized in answering only medical-related questions.
- **Context Memory**: The chatbot remembers the chat history and utilizes it to provide more coherent responses during the conversation.
- **User-Friendly Interface**: A simple and easy-to-use web interface built with Streamlit.

## Requirements
- **Python 3.7** or higher.
- An **API key from Groq** for the `ChatGroq` model.

## Installation

1. **Clone the repository** to your local machine:
   ```bash
   git clone https://github.com/umairjaffer/ai_doctor.git
   cd ai_doctor
   ```

2. **Install the required dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up your API key**:
   - Replace the placeholder `"your_api_key_here"` with your Groq API key in the code.

4. **Run the Streamlit app**:
   ```bash
   streamlit run app.py
   ```

   This will launch the AI Doctor chatbot on your local machine.

## Usage

1. Open the application in your browser after running it.
2. You can either:
   - **Type a medical-related question** in the text input box.
   - **Click the "Speak" button** to ask your question via voice (the application will use the microphone and convert your speech to text).
3. The chatbot will respond to your medical-related question with short and precise answers.
4. If the question is not related to medicine, the chatbot will respond with: 
   - *"I'm only trained to answer medical-related questions."*

## Example Usage
- **User**: "What are the symptoms of diabetes?"
  - **AI Doctor**: "Common symptoms include increased thirst, frequent urination, fatigue, and blurred vision."
  
- **User**: "How can I treat a cold?"
  - **AI Doctor**: "Rest, hydration, and over-the-counter medications can help alleviate symptoms of a cold."

- **User**: "What is the capital of France?"
  - **AI Doctor**: "I'm only trained to answer medical-related questions."

## Limitations
- **Medical-Only Responses**: The chatbot is only trained to answer medical-related questions. If you ask a non-medical question, it will respond with: *"I'm only trained to answer medical-related questions."*
- **Speech Recognition Accuracy**: The accuracy of speech recognition may vary depending on your microphone quality and background noise. The Google Speech API is used for speech-to-text conversion.
- **API Dependency**: The chatbot relies on the Groq API for generating responses. Ensure you have a stable internet connection for the API to function properly.
- **Model Dependency**: The model used in the chatbot, `mixtral-8x7b-32768`, is specifically chosen for medical-related responses. You will need an API key to access it.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments
- **Streamlit**: For providing an easy-to-use framework for creating the user interface.
- **Google Speech API**: For converting user speech into text.
- **Groq**: For providing the AI model to answer medical-related questions.
- **LangChain**: For managing the conversational flow and memory.

## requirements.txt

```plaintext
streamlit==1.41.1
langchain_groq==0.2.3
langchain==0.3.16
SpeechRecognition==3.14.1
PyAudio==0.2.14`
```