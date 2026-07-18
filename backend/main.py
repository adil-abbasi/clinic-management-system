from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.database.database import engine, Base

# Import Models
from app.models.doctor import Doctor
from app.models.patient import Patient
from app.models.opd_visit import OPDVisit

# Import Routes
from app.api.doctor_routes import router as doctor_router
from app.api.patient_routes import router as patient_router
from app.api.opd_routes import router as opd_router

app = FastAPI(
    title="Clinic Management System API",
    description="Offline Clinic Management Backend",
    version="1.0.0"
)

# Create Database Tables
Base.metadata.create_all(bind=engine)

# Register Routes
app.include_router(doctor_router)
app.include_router(patient_router)
app.include_router(opd_router)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
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
        "database": "Connected"
    }