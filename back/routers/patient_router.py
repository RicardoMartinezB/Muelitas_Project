from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from repositories.patient_repo import PatientRepository
from services.patient_service import PatientService
from schemas.patient import (
    PatientCreate,
    PatientUpdate,
    PatientResponse
)
from typing import List

router = APIRouter(prefix="/patients", tags=["Patients"])

@router