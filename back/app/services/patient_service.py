from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from fastapi import HTTPException, status
from doctor_muelitas.back.app.models.patient import Patient
from doctor_muelitas.back.app.schemas.patient import PatientCreate

def create_patient(db: Session, patient: PatientCreate) -> Patient:
    db_patient = Patient(**patient.model_dump())
    db.add(db_patient)
    try:
        db.commit()
        db.refresh(db_patient)
    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Patient with this email already exists"
        )
    return db_patient