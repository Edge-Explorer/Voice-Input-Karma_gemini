import streamlit as st
import requests
import json
import os
from dotenv import load_dotenv

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
    .stButton > button:hover {
        background: linear-gradient(45deg, #0072ff, #00c6ff);
        color: white;
    }
    .response-box {
        background-color: #1e1e26;
        padding: 20px;
        border-radius: 15px;
        border-left: 5px solid #0072ff;
        margin-top: 20px;
    }
    .footer {
        text-align: center;
        margin-top: 50px;
        color: #888;
    }
</style>
""", unsafe_allow_html=True)

# App Header
st.title("🕉️ Karma AI")
st.subheader("Spiritual Guidance from the Garud Puran")
st.write("Ask about your deeds, karma, and the cycle of life and death.")

# Sidebar for history or settings
with st.sidebar:
    st.header("Settings")
    st.info("Using Gemini 2.0 Flash for ultra-fast, wise responses.")
    if st.button("Clear History"):
        st.session_state.history = []

# Question Input
question = st.text_input("Enter your question:", placeholder="e.g., What happens to those who help the poor?")

if st.button("Consult the Sage"):
    if question:
        with st.spinner("Seeking wisdom from the scriptures..."):
            try:
                # Call our FastAPI backend
                response = requests.post(
                    "http://localhost:8000/api/ask",
                    json={"question": question}
                )
                
                if response.status_code == 200:
                    data = response.json()
                    answer = data.get("answer", "No answer received.")
                    
                    st.markdown(f'<div class="response-box">{answer}</div>', unsafe_allow_html=True)
                    
                    # Voice Output (Optional Feature)
                    if st.checkbox("Read out loud"):
                        st.info("Voice synthesis enabled.")
                else:
                    st.error("Failed to connect to the backend server.")
            except Exception as e:
                st.error(f"Error: {e}")
    else:
        st.warning("Please enter a question first.")

# Footer
st.markdown('<div class="footer">Made with 🙏 for Spiritual Awakening</div>', unsafe_allow_html=True)
