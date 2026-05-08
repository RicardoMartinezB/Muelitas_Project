from sqlalchemy import Column, Integer, DateTime, ForeignKey
from sqlachemy.orm import relationship
from app.core.database import Base
from datetime import datetime

class Appintment(Base):
    __tablename__ = 'appointments'

    id = Column(Integer, primary_key=True, index=True)
    appointment_time = Column(DateTime, nullable=False)
    patient_id = Column(Integer, ForeignKey('patients.id'))
    dentist_id = Column(Integer, ForeignKey('dentists.id'))
    
    patient = relationship("Patient", back_populates="appointments")
    dentist = relationship("Dentist", back_populates="appointments")