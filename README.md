# 🕉️ Karma AI: The Perfected Garud Puran Guide

This project is a high-performance, spiritually-focused AI application using **Gemini 2.0 Flash**, **PostgreSQL**, and **Streamlit**.

## 📁 Project Structure

```text
Voice-Input-Karma_gemini/
├── backend/                # FastAPI Logic & AI Core
│   ├── main.py             # Entry point (API)
│   ├── core/
│   │   ├── agent.py        # Gemini 2.0 Agent Logic
│   │   └── ingest.py       # ChromaDB Ingestion Service
│   ├── models/
│   │   └── interaction.py  # SQLAlchemy PostgreSQL Models
│   ├── alembic/            # Database Migrations
│   └── legacy/             # Original files from initial setup
├── frontend/
│   └── app.py              # Streamlit Premium Interface
├── data/
│   ├── chroma_db/          # Vector Storage (Search Engine)
│   └── Content_Storage_df.csv # Your Garud Puran Dataset
└── .env                    # System Configuration
```

## 🚀 Setup Instructions

### 1. Environment
Ensure your `.env` is configured with your **Gemini API Key** and **PostgreSQL Credentials**.

### 2. Database Migration (Alembic)
To set up your PostgreSQL tables:
```bash
cd backend
alembic upgrade head
```

### 3. Knowledge Ingestion (ChromaDB)
To load your CSV data into the AI's search engine:
```bash
cd backend
python core/ingest.py
```

### 4. Running the App
**Start the Backend:**
```bash
cd backend
python main.py
```

**Start the Streamlit Frontend:**
```bash
cd frontend
streamlit run app.py
```

## 🛠️ Perfection Highlights
- **Gemini 2.0 Flash**: Ultra-fast responses with deep spiritual insight.
- **RAG (Search Engine)**: Uses ChromaDB to ensure the AI answers based on the real Garud Puran text, not just guesses.
- **PostgreSQL**: Stores every interaction for history and analytics via pgAdmin 4.
- **Premium UI**: Dark-themed, modern Streamlit interface.
