from sqlalchemy.orm import Session

from app.models.opd_visit import OPDVisit
from app.models.patient import Patient
from app.models.doctor import Doctor


class OPDService:


    @staticmethod
    def get_token_slip(
        db: Session,
        visit_id: int
    ):

        visit = db.query(OPDVisit).filter(
            OPDVisit.id == visit_id
        ).first()


        if not visit:
            return None


        patient = db.query(Patient).filter(
            Patient.id == visit.patient_id
        ).first()


        doctor = db.query(Doctor).filter(
            Doctor.id == visit.doctor_id
        ).first()



        return {

            "token_number": visit.token_number,

            "patient_name": patient.name,
            "father_husband_name": patient.father_name,
            "age": patient.age,
            "gender": patient.gender,
            "phone": patient.phone,
            "patient_code": patient.patient_code,


            "doctor_name": doctor.name,
            "department": doctor.department,


            "visit_date": visit.visit_date,
            "visit_day": visit.visit_day,
            "visit_time": visit.visit_time,


            "consultation_fee": visit.consultation_fee,

            "status": visit.status
        }