from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from doctor_muelitas.back.app.schemas.patient import PatientCreate, PatientBase, PatientRead
from doctor_muelitas.back.app.services.patient_service import create_patient
from doctor_muelitas.back.app.core.database import get_db

router = APIRouter(
    prefix="/patients",
    tags=["Patients"]
)

@router.post("/", response_model=PatientRead, status_code=201)
def create_patient(patient: PatientCreate, db: Session = Depends(get_db)):
    return create_patient(db, patient)
    