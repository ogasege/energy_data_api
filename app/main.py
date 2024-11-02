from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from pydantic import BaseModel
from typing import List
from . import crud, models, schemas, database
import os


# Use environment variables or hardcoded values
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://admin:password@localhost/energy_data_db")

# Create a SQLAlchemy engine
engine = create_engine(DATABASE_URL)

# Create a configured "Session" class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

class DeviceCreate(BaseModel):
    name: str

# Create a base class for your models
Base = declarative_base()

app = FastAPI()

# Dependency to get the session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/devices/", response_model=List[schemas.DeviceSchema])
def list_devices(skip: int = 0, limit: int = 10, db: Session = Depends(database.get_db)):
    devices = crud.get_devices(db, skip=skip, limit=limit)
    return devices

@app.get("/devices/{device_id}", response_model=schemas.DeviceSchema)
def get_device(device_id: int, db: Session = Depends(database.get_db)):
    device = crud.get_device(db, device_id=device_id)
    if device is None:
        raise HTTPException(status_code=404, detail="Device not found")
    return device