from fastapi import FastAPI
from back.app.routers import patient_router

app = FastAPI(
    title="Doctor Muelitas API",
    version="0.1.0",
)

app.include_router(patient_router.router)