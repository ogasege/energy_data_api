from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Device(Base):
    __tablename__ = 'devices'
    device_id = Column(Integer, primary_key=True)
    device_name = Column(String, unique=True)
    description = Column(String)