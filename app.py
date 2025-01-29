import streamlit as st
import speech_recognition as sr
from langchain_groq import ChatGroq
from langchain.memory import ConversationBufferMemory
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate

# Initialize chatbot
api_key = 'Your Groq API KEY will be here'
llm = ChatGroq(
    api_key=api_key,
    model="mixtral-8x7b-32768",
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2,
)

# Memory to maintain context
memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

# Define prompt template
prompt = PromptTemplate(
    input_variables=["chat_history", "question"],
    template="""
    You are an AI doctor. Answer only medical-related questions with short and precise responses.
    If the question is not related to medicine, reply: 'I'm only trained to answer medical-related questions.'
    
    Chat history:
    {chat_history}
    
    Human: {question}
    AI Doctor:
    """
)

# Define LLM Chain
chain = LLMChain(llm=llm, prompt=prompt, memory=memory)

# Streamlit UI
st.title("AI Doctor Chatbot")
st.write("Ask medical-related questions, and I'll provide precise answers.")

# Speech Recognition Function
def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        st.write("Listening...")
        try:
            audio = recognizer.listen(source)
            text = recognizer.recognize_google(audio)
            return text
        except sr.UnknownValueError:
            return "Could not understand the audio. Please try again."
        except sr.RequestError:
            return "Could not request results. Please check your internet connection."

# User input options
user_input = st.text_input("Your question:", "")
if st.button("Speak 🔊"):
    user_input = recognize_speech()
    st.write("**You said:**", user_input)

if user_input:
    response = chain.run(user_input)
    st.write("**AI Doctor:**", response)
