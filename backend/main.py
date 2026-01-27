import os
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from core.agent import KarmaAgent
from models.interaction import SessionLocal, Interaction
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(title="Karma AI - API")

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize the AI Agent
agent = KarmaAgent()

class QuestionRequest(BaseModel):
    question: str

@app.post("/api/ask")
async def ask_question(request: QuestionRequest):
    try:
        # 1. Get answer and context from Gemini + ChromaDB
        answer, context = agent.solve(request.question)
        
        # 2. Save to PostgreSQL
        db = SessionLocal()
        try:
            new_interaction = Interaction(
                question=request.question,
                answer=answer,
                context_used=context
            )
            db.add(new_interaction)
            db.commit()
            db.refresh(new_interaction)
        except Exception as db_err:
            print(f"Database save error: {db_err}")
            # We continue even if DB save fails to not block the user
        finally:
            db.close()
            
        return {
            "answer": answer,
            "id": getattr(new_interaction, 'id', None)
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/history")
async def get_history():
    db = SessionLocal()
    interactions = db.query(Interaction).order_by(Interaction.created_at.desc()).limit(10).all()
    db.close()
    return interactions

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
