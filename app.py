import streamlit as st
import speech_recognition as sr
from langchain_groq import ChatGroq
from langchain.schema import SystemMessage, HumanMessage, AIMessage

# Set Streamlit page configuration
st.set_page_config(page_title="AI Doctor ChatBot")
st.title("AI Doctor")

# Initialize session state variables
if 'entered_prompt' not in st.session_state:
    st.session_state['entered_prompt'] = ""

if 'generated' not in st.session_state:
    st.session_state['generated'] = []  # Store AI responses

if 'past' not in st.session_state:
    st.session_state['past'] = []  # Store user inputs

# Function to handle speech input
def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        st.info("Listening... Speak now!")
        try:
            audio = recognizer.listen(source, timeout=5)
            text = recognizer.recognize_google(audio)
            st.session_state.entered_prompt = text  # Store recognized text
            st.success(f"Recognized: {text}")
        except sr.UnknownValueError:
            st.error("Sorry, I couldn't understand your speech.")
        except sr.RequestError:
            st.error("Speech recognition service is unavailable.")

# Define function to submit user input
def submit():
    st.session_state.entered_prompt = st.session_state.prompt_input
    st.session_state.prompt_input = ""

# Initialize the Groq AI model
api_key = "Enter Your Groq api here"  # Replace with your Groq API key
chat = ChatGroq(
    api_key=api_key,
    model="llama-3.3-70b-versatile",
    temperature=0.5,
    max_tokens=100
)

def build_message_list():
    """
    Build a list of messages including system, human, and AI messages.
    """
    messages = [SystemMessage(
        content="""You are an AI doctor. Answer only medical-related questions with short and precise responses.
                   If the question is not related to medicine, reply: 'I'm only trained to answer medical-related questions.'

                   IF user ask you to answer in Urdu language then you need to generate answers in Urdu
                   Otherwise stick with english.  

                    1. **Only answer disease-related questions.** Strictly avoid unrelated topics.  
                    2. If a user asks a **non-medical question**, politely steer the conversation back to diseases. Example:  
                    - User: "What's the weather today?"  
                    - AI: "I specialize in medical guidance. Do you have any health concerns?"  
                    3. **Keep responses short and medically accurate** (max 100 words).  
                    4. **Do not diagnose, prescribe, or make medical claims**—always recommend consulting a doctor.  
                    5. If symptoms seem serious, **urge immediate medical consultation.**  
                    6. If the user thanks you or ends the conversation, respond with a polite farewell. 
                    """
    )]

    # Add user and AI messages in order
    for i in range(len(st.session_state['past'])):
        messages.append(HumanMessage(content=st.session_state['past'][i]))
        if i < len(st.session_state['generated']):
            messages.append(AIMessage(content=st.session_state['generated'][i]))

    return messages

def generate_response():
    """
    Generate AI response using the ChatGroq model.
    """
    messages = build_message_list()
    ai_response = chat(messages)
    return ai_response.content if ai_response else "I'm sorry, I couldn't generate a response."

# Create a text input for user
st.text_input('YOU:', key='prompt_input', on_change=submit)

# Speech-to-Text button
if st.button("🎙️ Speak Now"):
    recognize_speech()

if st.session_state.entered_prompt:
    # Get user query
    user_query = st.session_state.entered_prompt

    # Append user query to past messages
    st.session_state.past.append(user_query)

    # Generate AI response
    output = generate_response()

    # Append AI response to generated responses
    st.session_state.generated.append(output)

# Display chat history using native Streamlit elements
for i in range(len(st.session_state['past']) - 1, -1, -1):  # Reverse order
    st.markdown(f"**You👨‍⚕️:** {st.session_state['past'][i]}")
    if i < len(st.session_state['generated']):
        st.markdown(f"**AI Doctor💉:** {st.session_state['generated'][i]}")
    st.divider()  # Adds a visual separation
