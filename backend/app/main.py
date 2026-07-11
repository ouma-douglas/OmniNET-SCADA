from fastapi import FastAPI
from sqlalchemy import text

from app.core.config import settings
from app.db.database import engine
from app.api.routers.devices import router as device_router


app = FastAPI(
    title=settings.APP_NAME,
    version=settings.VERSION,
)


# Register API routers
app.include_router(device_router)


@app.get("/")
def root():
    return {
        "application": settings.APP_NAME,
        "version": settings.VERSION,
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }


@app.get("/db-test")
def db_test():
    with engine.connect() as connection:
        result = connection.execute(text("SELECT version();"))
        version = result.scalar()

    return {
        "database": version
    }