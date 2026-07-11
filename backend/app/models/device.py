import enum
import uuid
from datetime import datetime

from sqlalchemy import Column, DateTime, Enum, String
from sqlalchemy.dialects.postgresql import UUID

from app.db.database import Base


class DeviceStatus(str, enum.Enum):
    ONLINE = "ONLINE"
    OFFLINE = "OFFLINE"
    WARNING = "WARNING"
    FAULT = "FAULT"
    MAINTENANCE = "MAINTENANCE"
    UNKNOWN = "UNKNOWN"


class DeviceType(str, enum.Enum):
    PLC = "PLC"
    RTU = "RTU"
    SENSOR = "SENSOR"
    METER = "METER"
    HMI = "HMI"
    GATEWAY = "GATEWAY"
    CAMERA = "CAMERA"
    OTHER = "OTHER"


class Device(Base):
    __tablename__ = "devices"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)

    name = Column(String(100), nullable=False)

    manufacturer = Column(String(100))

    model = Column(String(100))

    serial_number = Column(String(100), unique=True)

    ip_address = Column(String(50))

    protocol = Column(String(50))

    status = Column(
        Enum(DeviceStatus),
        default=DeviceStatus.UNKNOWN,
        nullable=False,
    )

    device_type = Column(
        Enum(DeviceType),
        nullable=False,
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow,
    )