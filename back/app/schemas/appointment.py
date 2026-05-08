from pydantic import BaseModel
from datetime import datetime

class AppointmentCreate(BaseModel):
    patient_id: int
    doctor_id: int
    appointment_time: datetime

class AppointmentRead(AppointmentCreate):
    id: int
    
    class Config:
        from_attributes = True