from sqlalchemy.orm import Session

from app.models.doctor import Doctor
from app.schemas.doctor import DoctorCreate, DoctorUpdate


class DoctorService:

    @staticmethod
    def create_doctor(
        db: Session,
        doctor: DoctorCreate
    ):

        db_doctor = Doctor(
            **doctor.model_dump()
        )

        db.add(db_doctor)
        db.commit()
        db.refresh(db_doctor)

        return db_doctor


    @staticmethod
    def get_all_doctors(
        db: Session
    ):

        return db.query(Doctor).all()


    @staticmethod
    def get_doctor(
        db: Session,
        doctor_id: int
    ):

        return db.query(Doctor).filter(
            Doctor.id == doctor_id
        ).first()


    @staticmethod
    def update_doctor(
        db: Session,
        doctor_id: int,
        doctor: DoctorUpdate
    ):

        db_doctor = db.query(Doctor).filter(
            Doctor.id == doctor_id
        ).first()

        if not db_doctor:
            return None


        for key, value in doctor.model_dump(
            exclude_unset=True
        ).items():

            setattr(
                db_doctor,
                key,
                value
            )


        db.commit()
        db.refresh(db_doctor)

        return db_doctor


    @staticmethod
    def delete_doctor(
        db: Session,
        doctor_id: int
    ):

        db_doctor = db.query(Doctor).filter(
            Doctor.id == doctor_id
        ).first()

        if not db_doctor:
            return None


        db_doctor.is_active = False

        db.commit()

        return db_doctor