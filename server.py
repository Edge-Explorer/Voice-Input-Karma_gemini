from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import uvicorn
from typing import Optional

app = FastAPI()

class QuestionRequest(BaseModel):
    question: str

class AnswerResponse(BaseModel):
    answer: str

@app.get("/")
def read_root():
    return {"message": "Q&A Server is running!"}

@app.post("/api/question")
def answer_question(question_request: QuestionRequest):
    # Simple example responses - in a real app, this would be connected to a model or database
    if not question_request.question:
        raise HTTPException(status_code=400, detail="Question cannot be empty")
    
    # This is where you would process the question with your actual logic
    # For demonstration, we'll use a simple dictionary of canned responses
    qa_pairs = {
        "what is your name": "I am a Q&A assistant.",
        "how are you": "I'm just a program, but thanks for asking!",
        "who created you": "I was created by a developer using FastAPI and React Native.",
        "what time is it": "I don't have access to real-time information.",
        "hello": "Hello! How can I help you today?",
    }
    
    # Convert to lowercase for case-insensitive matching
    question_lower = question_request.question.lower()
    
    # Try to find a direct match
    for q, a in qa_pairs.items():
        if q in question_lower:
            return {"answer": a}
    
    # Default response
    return {"answer": "I don't know the answer to that question."}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5000)