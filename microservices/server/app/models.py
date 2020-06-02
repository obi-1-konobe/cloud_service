from pydantic import BaseModel


class IndicatorsOUT(BaseModel):
    patient_id: int
    name: str
    gender: str
    doctor: str
    ward: str
    bunk: str
    date_in: str
    date_time: str
    temperature: float
    heartbeat: int
    pressure: int
    nrm: int


class IndicatorsIN(BaseModel):
    id: int
    patient_id: int
    name: str
    gender: str
    doctor: str
    ward: str
    bunk: str
    date_in: str
    date_time: str
    temperature: float
    heartbeat: int
    pressure: int
    nrm: int
