from pydantic import BaseModel, EmailStr
from datetime import date

class PatientCreate(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    phone: str | None
    date_of_birth: date | None

class PatientRead(PatientCreate):
    id: int
    
    class Config:
        from_attributes = True