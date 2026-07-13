import importlib.util

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.routes import router
from app.core.config import SAMPLE_DATA_DIR
from app.database.database import Base, engine
from app.models import QueryLog  # noqa: F401

app = FastAPI(title="AI SQL Analyst")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)


def _init_sample_database():
    script = SAMPLE_DATA_DIR / "create_database.py"
    spec = importlib.util.spec_from_file_location("create_database", script)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    module.create_database()


@app.on_event("startup")
def startup():
    _init_sample_database()
    Base.metadata.create_all(bind=engine)
