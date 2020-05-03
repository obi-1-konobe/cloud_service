from pydantic import BaseModel


class IndicatorsOUT(BaseModel):
    device_id: int
    datetime: str
    heartbeats: int
    temperature: int


class IndicatorsIN(BaseModel):
    id: int
    device_id: int
    datetime: str
    heartbeats: int
    temperature: int