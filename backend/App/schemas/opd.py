from pydantic import BaseModel
from datetime import date, datetime


class TokenSlipResponse(BaseModel):

    token_number: int

    patient_name: str
    father_husband_name: str
    age: int
    gender: str
    phone: str
    patient_code: str

    doctor_name: str
    department: str

    visit_date: date
    visit_day: str
    visit_time: datetime

    consultation_fee: float

    status: str

    class Config:
        from_attributes = True