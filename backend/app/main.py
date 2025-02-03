# backend/app/main.py

from fastapi import FastAPI

# Initialize the FastAPI app
app = FastAPI(title="EduAgent Backend API")

# Define a basic endpoint for testing
@app.get("/")
async def read_root():
    return {"message": "Welcome to EduAgent API!"}

# Additional test endpoint to check the API health
@app.get("/health")
async def health_check():
    return {"status": "ok"}
