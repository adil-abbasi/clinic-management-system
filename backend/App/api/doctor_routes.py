from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.dependencies import get_db
from app.schemas.doctor import DoctorCreate, DoctorResponse, DoctorUpdate
from app.services.doctor_service import DoctorService

router = APIRouter(
    prefix="/doctors",
    tags=["Doctors"]
)


@router.post("/", response_model=DoctorResponse)
def create_doctor(
    doctor: DoctorCreate,
    db: Session = Depends(get_db)
):
    return DoctorService.create_doctor(db, doctor)


@router.get("/", response_model=list[DoctorResponse])
def get_doctors(
    db: Session = Depends(get_db)
):
    return DoctorService.get_all_doctors(db)


@router.get("/{doctor_id}", response_model=DoctorResponse)
def get_doctor(
    doctor_id: int,
    db: Session = Depends(get_db)
):
    doctor = DoctorService.get_doctor(db, doctor_id)

    if not doctor:
        raise HTTPException(status_code=404, detail="Doctor not found")

    return doctor


@router.put("/{doctor_id}", response_model=DoctorResponse)
def update_doctor(
    doctor_id: int,
    doctor: DoctorUpdate,
    db: Session = Depends(get_db)
):
    updated = DoctorService.update_doctor(db, doctor_id, doctor)

    if not updated:
        raise HTTPException(status_code=404, detail="Doctor not found")

    return updated


@router.delete("/{doctor_id}")
def delete_doctor(
    doctor_id: int,
    db: Session = Depends(get_db)
):
    deleted = DoctorService.delete_doctor(db, doctor_id)

    if not deleted:
        raise HTTPException(status_code=404, detail="Doctor not found")

    return {"message": "Doctor deactivated successfully"}