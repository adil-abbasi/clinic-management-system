from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.database.database import engine, Base
from app.models.doctor import Doctor
from app.api.doctor_routes import router as doctor_router
from app.models.patient import Patient
from app.models.opd_visit import OPDVisit
from app.api.patient_routes import router as patient_router
app.include_router(patient_router)
app.include_router(doctor_router, prefix="/api/v1")
app = FastAPI(
    
    title="Clinic Management System API",
    description="Offline Clinic Management Backend",
    version="1.0.0"
)
Base.metadata.create_all(bind=engine)
app.include_router(doctor_router)
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