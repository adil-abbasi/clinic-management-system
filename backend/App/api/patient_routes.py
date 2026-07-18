from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.dependencies import get_db
from app.schemas.patient import (
    PatientCreate,
    PatientUpdate,
    PatientResponse,
)
from app.services.patient_service import PatientService

router = APIRouter(
    prefix="/patients",
    tags=["Patients"],
)


@router.post("/", response_model=PatientResponse)
def create_patient(
    patient: PatientCreate,
    db: Session = Depends(get_db),
):
    return PatientService.create(db, patient)


@router.get("/", response_model=list[PatientResponse])
def get_patients(
    db: Session = Depends(get_db),
):
    return PatientService.get_all(db)


@router.get("/{patient_id}", response_model=PatientResponse)
def get_patient(
    patient_id: int,
    db: Session = Depends(get_db),
):
    patient = PatientService.get(db, patient_id)

    if not patient:
        raise HTTPException(404, "Patient not found")

    return patient


@router.put("/{patient_id}", response_model=PatientResponse)
def update_patient(
    patient_id: int,
    patient: PatientUpdate,
    db: Session = Depends(get_db),
):
    updated = PatientService.update(
        db,
        patient_id,
        patient,
    )

    if not updated:
        raise HTTPException(404, "Patient not found")

    return updated


@router.delete("/{patient_id}")
def delete_patient(
    patient_id: int,
    db: Session = Depends(get_db),
):
    deleted = PatientService.delete(
        db,
        patient_id,
    )

    if not deleted:
        raise HTTPException(404, "Patient not found")

    return {
        "message": "Patient deactivated successfully"
    }