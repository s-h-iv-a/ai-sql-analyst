from fastapi import FastAPI

from app.api.routes import router
from app.core.config import settings

from app.database.database import Base, engine

from app.models.query_log import QueryLog


Base.metadata.create_all(
    bind=engine
)


app = FastAPI(
    title=settings.APP_NAME,
    version="1.0.0"
)


app.include_router(router)


@app.get("/")
async def root():

    return {
        "message": "AI SQL Analyst Backend Running"
    }