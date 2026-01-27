import streamlit as st
import requests
import json
import os
import speech_recognition as sr
from dotenv import load_dotenv
from io import BytesIO
from gtts import gTTS

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
        padding: 25px;
        border-radius: 15px;
        border-left: 5px solid #0072ff;
        margin-top: 20px;
        font-size: 1.1rem;
        line-height: 1.8;
        color: #e0e0e0;
        box-shadow: 0 4px 15px rgba(0,0,0,0.3);
    }
    .footer {
        text-align: center;
        margin-top: 50px;
        color: #888;
        font-size: 0.8rem;
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state
if 'answer' not in st.session_state:
    st.session_state.answer = ""
if 'voice_text' not in st.session_state:
    st.session_state.voice_text = ""

# App Header
st.title("🕉️ Karma AI")
st.subheader("Spiritual Guidance from the Garud Puran")

# Voice Input Section
col1, col2 = st.columns([4, 1])

with col2:
    if st.button("🎤 Ask"):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            st.toast("Listening... Speak now!")
            try:
                # Adjust for ambient noise
                r.adjust_for_ambient_noise(source, duration=0.5)
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
        with st.spinner("Seeking wisdom from the ancient scriptures..."):
            try:
                response = requests.post("http://localhost:8000/api/ask", json={"question": question})
                if response.status_code == 200:
                    st.session_state.answer = response.json().get("answer", "")
                else:
                    st.error("The sage is currently deep in meditation (Backend unreachable).")
            except Exception as e:
                st.error(f"Error: {e}")
    else:
        st.warning("Please enter a question or speak into the microphone.")

# Display Answer and Voice Output
if st.session_state.answer:
    st.markdown(f'<div class="response-box">{st.session_state.answer}</div>', unsafe_allow_html=True)
    
    st.write("---")
    colA, colB = st.columns([1, 2])
    
    with colA:
        if st.button("🔊 Read Aloud"):
            with st.spinner("Preparing audio..."):
                try:
                    tts = gTTS(text=st.session_state.answer, lang='en')
                    fp = BytesIO()
                    tts.write_to_fp(fp)
                    st.audio(fp)
                except Exception as e:
                    st.error("Audio generation failed.")

# Footer
st.markdown('<div class="footer">Made with 🙏 for Spiritual Awakening | Powered by Gemini 2.0 Flash</div>', unsafe_allow_html=True)
