# backend/app/models.py

from sqlalchemy import Column, Integer, Text
from .database import Base

class ProcessedContent(Base):
    __tablename__ = "processed_content"
    
    id = Column(Integer, primary_key=True, index=True)
    raw_text = Column(Text, nullable=False)
    summary = Column(Text, nullable=True)
    explanation = Column(Text, nullable=True)
    quiz = Column(Text, nullable=True)
