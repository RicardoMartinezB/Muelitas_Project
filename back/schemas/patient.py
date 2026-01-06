from pydantic import BaseModel
from datetime import date
from typing import Optional

class PatientBase(BaseModel):
    name: str
    phone: Optional[str] = None
    date_of_birth: Optional[date] = None

class PatientCreate(PatientBase):
    pass

class PatientUpdate(PatientBase):
    pass

class PatientUpdate(PatientBase):
    pass

class PatientResponse(PatientBase):
    id: int

    class Config:
        from_attributes = True