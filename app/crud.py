from sqlalchemy.orm import Session
from . import models

def get_devices(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Device).offset(skip).limit(limit).all()