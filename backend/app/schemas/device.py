from uuid import UUID
from datetime import datetime

from pydantic import BaseModel

from app.models.device import DeviceStatus, DeviceType


class DeviceBase(BaseModel):
    name: str

    manufacturer: str | None = None

    model: str | None = None

    serial_number: str | None = None

    ip_address: str | None = None

    protocol: str | None = None

    status: DeviceStatus = DeviceStatus.UNKNOWN

    device_type: DeviceType


class DeviceCreate(DeviceBase):
    """
    Schema used when registering a new device.
    """
    pass


class DeviceResponse(DeviceBase):
    """
    Schema returned by the API.
    """

    id: UUID

    created_at: datetime | None = None

    class Config:
        from_attributes = True