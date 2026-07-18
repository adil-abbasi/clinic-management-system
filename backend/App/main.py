from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.database.database import engine, Base
from app.models.doctor import Doctor

app = FastAPI(
    
    title="Clinic Management System API",
    description="Offline Clinic Management Backend",
    version="1.0.0"
)
Base.metadata.create_all(bind=engine)

# Allow Electron/React frontend to access the backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # We will secure this later
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def home():
    return {
        "message": "Clinic Management System Backend Running Successfully"
    }


@app.get("/health")
def health():
    return {
        "status": "OK",
        "database": "Not Connected Yet"
    }