from pydantic import BaseModel
from typing import Any


class QueryResponse(BaseModel):

    sql: str

    explanation: str

    results: list[Any]

    chart: dict