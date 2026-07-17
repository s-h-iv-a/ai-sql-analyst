from dotenv import load_dotenv
import os

load_dotenv()


class Settings:

    APP_NAME = os.getenv(
        "APP_NAME",
        "AI SQL Analyst"
    )

    GOOGLE_API_KEY = os.getenv(
        "GOOGLE_API_KEY"
    )

    DATABASE_URL = os.getenv(
        "DATABASE_URL",
        "sqlite:////app/sample.db"
    )

    MODEL_NAME = os.getenv(
        "MODEL_NAME",
        "gemini-2.0-flash"
    )

    DEBUG = os.getenv(
        "DEBUG",
        "False"
    ).lower() == "true"


settings = Settings()