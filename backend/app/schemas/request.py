from typing import Any

from pydantic import BaseModel


class QueryRequest(BaseModel):
    question: str
