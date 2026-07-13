import os
from pathlib import Path

from dotenv import load_dotenv
from pydantic import BaseModel

load_dotenv(Path(__file__).resolve().parents[2] / ".env")

PROJECT_ROOT = Path(__file__).resolve().parents[3]
SAMPLE_DATA_DIR = Path(os.getenv("SAMPLE_DATA_DIR", PROJECT_ROOT / "sample_data"))
DATABASE_PATH = SAMPLE_DATA_DIR / "sales.db"


class Settings(BaseModel):
    app_name: str = "AI SQL Analyst"
    database_url: str = f"sqlite:///{DATABASE_PATH}"
    openai_api_key: str = ""
    openai_model: str = "gpt-4o-mini"


settings = Settings(
    openai_api_key=os.getenv("OPENAI_API_KEY", ""),
    openai_model=os.getenv("OPENAI_MODEL", "gpt-4o-mini"),
)
