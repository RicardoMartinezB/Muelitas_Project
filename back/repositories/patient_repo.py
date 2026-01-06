from sqlalchemy.orm import Session
from models.patient import Patient

class PatientRepository:
    def __init__(self, db: Session):
        self.db = db
    
    def get_all(self):
        return self.db.query(Patient).all()

    def get_patient_by_id(self, patient_id: int):
        return self.db.query(Patient).filter(Patient.id == patient_id).first()
    
    def create(self, patient: Patient):
        self.db.add(patient)
        self.db.commit()
        self.db.refresh(patient)
        return patient
    
    def update(self, patient: Patient):
        self.db.commit()
        self.db.refresh(patient)
        return patient
    
    def delete(self, patient: Patient):
        self.db.delete(patient)
        self.db.commit()