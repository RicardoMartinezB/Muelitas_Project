from models.patient import Patient
from repositories.patient_repo import PatientRepository
from schemas.patient import PatientCreate, PatientUpdate

class PatientService:
    def __init__(self, repo: PatientRepository):
        self.repo = repo

    def get_all(self):
        return self.repo.get_all()
    
    def get_by_id(self, patient_id: int):
        patient = self.repo.get_patient_by_id(patient_id)
        if not patient:
            raise ValueError("Patient not found")
        return patient
    
    def create(self, data: PatientCreate):
        if data.phone and len(data.phone) < 10:
            raise ValueError("Phone number too short")

        patient = Patient(**data.model_dump())
        return self.repo.create(patient)
    
    def update(self, patient_id: int, data: PatientUpdate):
        patient = self.get_by_id(patient_id)
        
        for field, value in data.model_dump(exclude_unset=True).items():
            setattr(patient, field, value)

        return self.repo.update(patient)
    
    def delete(self, patient_id: int):
        patient = self.get_by_id(patient_id)
        self.repo.delete(patient)