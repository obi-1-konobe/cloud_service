from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Float
from sqlalchemy.orm import relationship

from .database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)

    items = relationship("Item", back_populates="owner")


class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    owner_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User", back_populates="items")
    indicators = relationship("Indicators", back_populates='device')


class Indicators(Base):
    __tablename__ = 'indicators'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    gender = Column(String, index=True)
    doctor = Column(String, index=True)
    ward = Column(String, index=True)
    bunk = Column(String, index=True)
    date_in = Column(String, index=True)
    date_time = Column(String, index=True)
    heartbeat = Column(Integer, index=True)
    temperature = Column(Float, index=True)
    pressure = Column(Integer, index=True)
    nrm = Column(Integer, index=True)
    patient_id = Column(Integer, ForeignKey("items.id"))

    device = relationship("Item", back_populates="indicators")