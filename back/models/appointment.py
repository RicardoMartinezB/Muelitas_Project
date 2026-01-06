class Appintment(Base):
    __tablename__ = 'appointments'

    id = Column(Integer, primary_key=True)
    patient_id = Column(Integer, ForeignKey('patients.id'), nullable=False)
    dentist_id = Column(Integer, ForeignKey('dentists.id'), nullable=False)
    appointment_date = Column(DateTime, nullable=False)
    status = Column(String(20), nullable=False, default='scheduled')