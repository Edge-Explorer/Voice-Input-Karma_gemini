from sqlalchemy import Column, Integer, Text, DateTime, create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker
import datetime
import os
from dotenv import load_dotenv

# Find project root
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
load_dotenv(os.path.join(BASE_DIR, ".env"))

DATABASE_URL = os.getenv("DATABASE_URL")

class Base(DeclarativeBase):
    pass

class Interaction(Base):
    __tablename__ = "interactions"

    id = Column(Integer, primary_key=True, index=True)
    question = Column(Text, nullable=False)
    answer = Column(Text, nullable=False)
    context_used = Column(Text, nullable=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
