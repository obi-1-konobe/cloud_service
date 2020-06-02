from typing import List

from pydantic import BaseModel


class IndicatorBase(BaseModel):
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


class IndicatorCreate(IndicatorBase):
    pass


class Indicator(IndicatorBase):
    id: int
    patient_id: int

    class Config:
        orm_mode = True


class ItemBase(BaseModel):
    title: str
    description: str = None


class ItemCreate(ItemBase):
    pass


class Item(ItemBase):
    id: int
    owner_id: int
    indicators: List[Indicator] = []

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    is_active: bool
    items: List[Item] = []

    class Config:
        orm_mode = True
