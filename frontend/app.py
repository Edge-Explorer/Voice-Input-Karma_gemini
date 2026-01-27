import streamlit as st
import requests
import json
import os
import speech_recognition as sr
from dotenv import load_dotenv
from io import BytesIO

load_dotenv()

# Page configuration
st.set_page_config(
    page_title="Karma AI - Garud Puran Guide",
    page_icon="🕉️",
    layout="centered"
)

# Custom CSS for Premium Look
st.markdown("""
<style>
    .main {
        background-color: #0e1117;
        color: #ffffff;
    }
    .stTextInput > div > div > input {
        background-color: #262730;
        color: #ffffff;
        border-radius: 10px;
    }
    .stButton > button {
        width: 100%;
        border-radius: 10px;
        background: linear-gradient(45deg, #00c6ff, #0072ff);
        color: white;
        font-weight: bold;
        border: none;
        padding: 0.5rem;
    }
    .response-box {
        background-color: #1e1e26;
        padding: 20px;
        border-radius: 15px;
        border-left: 5px solid #0072ff;
        margin-top: 20px;
        font-size: 1.1rem;
        line-height: 1.6;
    }
    .voice-btn-container {
        display: flex;
        gap: 10px;
        margin-bottom: 20px;
    }
</style>
""", unsafe_allow_html=True)

# App Header
st.title("🕉️ Karma AI")
st.subheader("Spiritual Guidance from the Garud Puran")

# Initialize session state for text input if not exists
if 'voice_text' not in st.session_state:
    st.session_state.voice_text = ""

# Voice Input Section
col1, col2 = st.columns([4, 1])

with col2:
    if st.button("🎤 Ask"):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            st.toast("Listening... Speak now!")
            try:
                audio = r.listen(source, timeout=5)
                text = r.recognize_google(audio)
                st.session_state.voice_text = text
            except Exception as e:
                st.error("Could not understand audio.")

with col1:
    question = st.text_input("Enter your question:", value=st.session_state.voice_text, placeholder="Ask about karma, swarg, or nark...")

# Submit Button
if st.button("Consult the Sage"):
    if question:
        with st.spinner("Seeking wisdom..."):
            try:
                response = requests.post("http://localhost:8000/api/ask", json={"question": question})
                if response.status_code == 200:
                    answer = response.json().get("answer", "")
                    st.markdown(f'<div class="response-box">{answer}</div>', unsafe_allow_html=True)
                    
                    # Voice Output (Read Aloud)
                    st.write("---")
                    if st.button("🔊 Read Aloud"):
                        import pyttsx3
                        engine = pyttsx3.init()
                        engine.say(answer)
                        engine.runAndWait()
                else:
                    st.error("Backend connection failed.")
            except Exception as e:
                st.error(f"Error: {e}")
    else:
        st.warning("Please enter a question or use the microphone.")

# Footer
st.markdown('<div class="footer">Made with 🙏 for Spiritual Awakening</div>', unsafe_allow_html=True)
