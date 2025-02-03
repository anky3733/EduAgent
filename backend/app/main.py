# backend/app/main.py

from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

# Import our database session and models
from .database import engine, SessionLocal, Base
from .models import ProcessedContent

# Create all tables (if they don't exist already)
Base.metadata.create_all(bind=engine)

app = FastAPI(title="EduAgent Backend API")

# Dependency to get a DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
async def read_root():
    return {"message": "Welcome to EduAgent API!"}

@app.get("/health")
async def health_check():
    return {"status": "ok"}

# "Hello World" endpoint that interacts with the database
@app.get("/db_test")
async def db_test(db: Session = Depends(get_db)):
    # Create a dummy record
    dummy = ProcessedContent(
        raw_text="Hello World",
        summary="Test Summary",
        explanation="Test Explanation",
        quiz="Test Quiz"
    )
    db.add(dummy)
    db.commit()
    db.refresh(dummy)
    
    # Query the first record from the table
    result = db.query(ProcessedContent).first()
    return {
        "record": {
            "id": result.id,
            "raw_text": result.raw_text,
            "summary": result.summary,
            "explanation": result.explanation,
            "quiz": result.quiz
        }
    }
