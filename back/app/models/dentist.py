from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship
from app.core.database import Base
from datetime import datetime

class Dentist(Base):
    __tablename__ = 'dentists'

    id = Column(Integer, primary_key=True, Inddex=True)
    full_name = Column(String(150), nullable=False)
    specialty = Column(String(100), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    appointments = relationship("Appointment", back_populates="dentist")