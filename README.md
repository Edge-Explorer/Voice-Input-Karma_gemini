# 🕉️ Karma AI: The Perfected Garud Puran Guide

A professional, high-performance spiritual AI assistant powered by **Gemini 2.0 Flash**, **PostgreSQL**, and **Streamlit**. Karma AI analyzes your deeds based on the ancient wisdom of the Garud Puran, offering guidance on Karma, Swarg (Heaven), and Nark (Hell).

---

## ✨ Features

- **🚀 Gemini 2.0 Flash**: Ultra-fast, intelligent spiritual insights.
- **📚 Agentic RAG**: Uses ChromaDB to ensure every answer is grounded in high-quality Garud Puran datasets.
- **🎙️ Voice-First Interaction**: 
  - **Voice Input**: Speak your questions naturally.
  - **Voice Output**: Listen to AI-generated spiritual summaries.
- **🏛️ Persistent Memory**: Every interaction is stored in **PostgreSQL** for your personal spiritual history.
- **💎 Premium UI**: A sleek, dark-themed Streamlit interface designed for focus and peace.

---

## 📁 Project Structure

```text
Voice-Input-Karma_gemini/
├── backend/                # FastAPI Logic & AI Core
│   ├── main.py             # Entry point (API)
│   ├── core/
│   │   ├── agent.py        # Gemini 2.0 SDK (+ google-genai)
│   │   └── ingest.py       # Knowledge Base Ingestion
│   ├── models/
│   │   └── interaction.py  # SQLAlchemy PostgreSQL Models
│   └── alembic/            # Database Migrations
├── frontend/
│   └── app.py              # Streamlit Premium Interface (Voice STT/TTS)
├── data/
│   ├── chroma_db/          # Vector Search Index (Ignored by Git)
│   └── Content_Storage_df.csv # Garud Puran Knowledge Base
├── requirements.txt        # Project Dependencies
└── .env                    # System Config (Ignored by Git)
```

---

## 🛠️ Setup Instructions

### 1. Environment Configuration
Create a `.env` file in the root directory (refer to `.env.example`):
```text
GEMINI_API_KEY=your_key_here
DATABASE_URL=postgresql://user:password@localhost:5432/Karam-gemini
```

### 2. Database Setup (Alembic)
Initialize your PostgreSQL tables:
```bash
cd backend
alembic upgrade head
```

### 3. Knowledge Ingestion
Load the Garud Puran dataset into the AI search engine:
```bash
python backend/core/ingest.py
```

### 4. Run the Application
**Start Backend:**
```bash
python backend/main.py
```

**Start Frontend:**
```bash
streamlit run frontend/app.py
```

---

## 🛡️ Sanity & Security Check
- **Secrets Protocol**: `.env` and `env/` folders are strictly excluded via `.gitignore`.
- **Data Privacy**: Local ChromaDB vector stores and user data CSVs are excluded from version control.
- **Code Integrity**: Using the latest `google-genai` SDK for future-proof performance.

---

## 🙏 Credits & Appreciation
Built with a passion for AI and Spiritual Awakening.
**"As you sow, so shall you reap"**
