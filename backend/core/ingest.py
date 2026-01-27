import pandas as pd
import chromadb
from chromadb.utils import embedding_functions
import os
from dotenv import load_dotenv

# Find project root
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
load_dotenv(os.path.join(BASE_DIR, ".env"))

def ingest_data():
    csv_path = os.path.join(BASE_DIR, "data", "Content_Storage_df.csv")
    chroma_path = os.path.join(BASE_DIR, "data", "chroma_db")
    
    if not os.path.exists(csv_path):
        print(f"Error: CSV file not found at {csv_path}")
        return

    print(f"Loading data from {csv_path}...")
    df = pd.read_csv(csv_path)
    
    # Assume the CSV has a column with text content, adjust if needed
    # Let's say it's the first column or a column named 'content'
    content_col = df.columns[0]
    documents = df[content_col].astype(str).tolist()
    ids = [f"id_{i}" for i in range(len(documents))]

    print(f"Initializing ChromaDB at {chroma_path}...")
    client = chromadb.PersistentClient(path=chroma_path)
    
    # Using default embedding function (HuggingFace)
    emb_fn = embedding_functions.DefaultEmbeddingFunction()
    
    collection = client.get_or_create_collection(
        name="karma_embeddings", 
        embedding_function=emb_fn
    )

    print(f"Ingesting {len(documents)} documents into ChromaDB. This may take a moment...")
    
    # Ingest in batches to avoid memory/API limits
    batch_size = 100
    for i in range(0, len(documents), batch_size):
        batch_docs = documents[i:i + batch_size]
        batch_ids = ids[i:i + batch_size]
        collection.add(
            documents=batch_docs,
            ids=batch_ids
        )
        print(f"Batch {i//batch_size + 1} complete.")

    print("Ingestion complete!")

if __name__ == "__main__":
    ingest_data()
