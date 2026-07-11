\# OmniNET-SCADA Backend



Industrial SCADA monitoring and device management platform built with FastAPI, PostgreSQL, and SQLAlchemy.



\## Project Overview



OmniNET-SCADA is a modern SCADA platform designed for monitoring, managing, and communicating with industrial assets such as PLCs, RTUs, sensors, meters, HMIs, and gateways.



The backend provides the foundation for:



\- Device registration and management

\- Industrial asset tracking

\- Real-time monitoring (future implementation)

\- Alarm management (future implementation)

\- Telemetry processing (future implementation)



\---



\# Current Development Status



\## Day 4 Complete ✅



Implemented:



\- FastAPI backend foundation

\- PostgreSQL database integration

\- SQLAlchemy ORM configuration

\- Alembic database migration system

\- Device asset management database model

\- Device API foundation

\- Swagger API documentation



\---



\# System Architecture



```text

Client / SCADA Dashboard

&#x20;         |

&#x20;         |

&#x20;      FastAPI

&#x20;         |

&#x20;         |

&#x20;   API Routers

&#x20;         |

&#x20;         |

&#x20;Pydantic Schemas

&#x20;         |

&#x20;         |

SQLAlchemy ORM Models

&#x20;         |

&#x20;         |

Alembic Migration Engine

&#x20;         |

&#x20;         |

&#x20;     PostgreSQL

```



\---



\# Backend Structure



```text

backend

│

├── app

│   ├── api

│   │   └── routers

│   │       └── devices.py

│   │

│   ├── core

│   │   └── config.py

│   │

│   ├── db

│   │   └── database.py

│   │

│   ├── models

│   │   └── device.py

│   │

│   ├── schemas

│   │   └── device.py

│   │

│   └── main.py

│

├── alembic

├── alembic.ini

├── requirements.txt

└── README.md

```



\---



\# Database



\## PostgreSQL Database



Database:



```text

omninet\_scada

```



\## Current Tables



\### devices



Stores registered SCADA equipment.



Fields:



```text

id              UUID primary key

name            Device name

manufacturer    Equipment manufacturer

model           Device model

serial\_number   Unique equipment identifier

ip\_address      Network address

protocol        Communication protocol

status          Operational status

device\_type     Equipment category

created\_at      Registration timestamp

```



\---



\# Supported Device Types



Currently supported:



```text

PLC

RTU

SENSOR

METER

HMI

GATEWAY

CAMERA

OTHER

```



\---



\# Device Status Monitoring



Supported states:



```text

ONLINE

OFFLINE

WARNING

FAULT

MAINTENANCE

UNKNOWN

```



\---



\# API Endpoints



\## Root



```http

GET /

```



Returns application information.



\---



\## Health Check



```http

GET /health

```



Checks backend availability.



\---



\## Database Test



```http

GET /db-test

```



Verifies PostgreSQL connectivity.



\---



\## Device API



\### Retrieve Devices



```http

GET /devices/

```



Returns registered SCADA devices from PostgreSQL.



\---



\# Running the Backend



\## Activate Virtual Environment



Windows:



```powershell

.\\venv\\Scripts\\activate

```



\---



\## Install Dependencies



```powershell

pip install -r requirements.txt

```



\---



\## Apply Database Migrations



```powershell

python -m alembic upgrade head

```



\---



\## Run Application



```powershell

uvicorn app.main:app --reload

```



\---



\# API Documentation



Swagger UI:



```text

http://127.0.0.1:8000/docs

```



\---



\# Development Roadmap



\## Completed



✅ Backend foundation  

✅ Database integration  

✅ Device model  

✅ Migration system  

✅ Initial API routing  



\## Upcoming



\- Device CRUD operations

\- MQTT communication layer

\- Real-time telemetry ingestion

\- Alarm management

\- User authentication

\- SCADA dashboard interface

\- Data visualization

\- Industrial protocol integration



\---



\# Technology Stack



\## Backend



\- Python

\- FastAPI

\- SQLAlchemy

\- Alembic



\## Database



\- PostgreSQL



\## Future Communication Protocols



\- MQTT

\- Modbus TCP

\- OPC UA



\---



\# Project Milestone



Current milestone:



\*\*Day 4 - Backend Database Foundation Complete\*\*



Next milestone:



\*\*Day 5 - Device CRUD API and telemetry preparation\*\*

