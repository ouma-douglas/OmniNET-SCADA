from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.models.device import Device


router = APIRouter(
    prefix="/devices",
    tags=["Devices"]
)


@router.get("/")
def get_devices(db: Session = Depends(get_db)):

    devices = db.query(Device).all()

    return devices