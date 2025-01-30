import streamlit as st
import speech_recognition as sr
from langchain_groq import ChatGroq
from langchain.schema import SystemMessage, HumanMessage, AIMessage

# Set up the Streamlit page
st.set_page_config(page_title="AI Doctor ChatBot")
st.title("🩺 AI Doctor ChatBot")

# Initialize session state
if 'entered_prompt' not in st.session_state:
    st.session_state['entered_prompt'] = ""
if 'generated' not in st.session_state:
    st.session_state['generated'] = []  # Store AI responses
if 'past' not in st.session_state:
    st.session_state['past'] = []  # Store user inputs

# Initialize the Groq AI model
api_key = "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"  # Replace with your Groq API key
chat = ChatGroq(api_key=api_key, model="llama-3.3-70b-versatile", temperature=0.5, max_tokens=100)

def recognize_speech():
    """Recognize speech from the microphone input."""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        st.info("🎙️ Listening... Speak now!")
        try:
            audio = recognizer.listen(source, timeout=5)
            text = recognizer.recognize_google(audio)
            st.session_state.entered_prompt = text  # Store recognized text
            st.success(f"✅ Recognized: {text}")
        except sr.UnknownValueError:
            st.error("❌ Sorry, I couldn't understand your speech.")
        except sr.RequestError:
            st.error("❌ Speech recognition service is unavailable.")

def build_message_list():
    """Build a list of messages including system, human, and AI messages."""
    messages = [SystemMessage(content="""
        You are an AI doctor. Answer only medical-related questions with short and precise responses.
        If the question is not related to medicine, reply: 'I'm only trained to answer medical-related questions.'
        """)]

    for i, user_message in enumerate(st.session_state['past']):
        messages.append(HumanMessage(content=user_message))
        if i < len(st.session_state['generated']):
            messages.append(AIMessage(content=st.session_state['generated'][i]))

    return messages

def generate_response():
    """Generate AI response using the ChatGroq model."""
    messages = build_message_list()
    with st.spinner("💬 Generating response..."):
        ai_response = chat(messages)
    return ai_response.content if ai_response else "I'm sorry, I couldn't generate a response."

def submit():
    """Handle user text input submission."""
    st.session_state.entered_prompt = st.session_state.prompt_input
    st.session_state.prompt_input = ""

# Display UI
st.text_input('**You:**', key='prompt_input', on_change=submit)

if st.button("🎙️Speak Now"):
    recognize_speech()

if st.session_state.entered_prompt:
    user_query = st.session_state.entered_prompt
    st.session_state.past.append(user_query)
    output = generate_response()
    st.session_state.generated.append(output)
    st.session_state.entered_prompt = ""

for i in range(len(st.session_state['past']) - 1, -1, -1):  # Reverse order
    st.markdown(f"**You:** {st.session_state['past'][i]}")
    if i < len(st.session_state['generated']):
        st.markdown(f"**AI Doctor:** {st.session_state['generated'][i]}")
    st.divider()
