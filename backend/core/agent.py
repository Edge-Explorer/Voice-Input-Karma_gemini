import google.generativeai as genai
import chromadb
import os
from dotenv import load_dotenv

# Find project root
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
load_dotenv(os.path.join(BASE_DIR, ".env"))

class KarmaAgent:
    def __init__(self):
        genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
        self.model = genai.GenerativeModel("gemini-2.0-flash")
        
        # Initialize ChromaDB with absolute path
        chroma_path = os.path.join(BASE_DIR, "data", "chroma_db")
        self.chroma_client = chromadb.PersistentClient(path=chroma_path)
        try:
            self.collection = self.chroma_client.get_collection("karma_embeddings")
        except:
            print("Warning: Collection 'karma_embeddings' not found. Please run ingestion script.")
            self.collection = None

    def get_context(self, query):
        if not self.collection:
            return ""
        results = self.collection.query(query_texts=[query], n_results=3)
        return " ".join(results['documents'][0]) if results['documents'] else ""

    def solve(self, question):
        context = self.get_context(question)
        
        prompt = f"""
        System: You are an AI assistant specialized in the Garud Puran.
        Context: {context}
        User Question: {question}
        
        Provide a wise and spiritually accurate response.
        """
        
        response = self.model.generate_content(prompt)
        return response.text, context
