from typing import Any

from pydantic import BaseModel


class QueryResponse(BaseModel):
    question: str
    sql: str
    results: list[dict[str, Any]]
    row_count: int
    explanation: str
    chart: dict[str, Any] | None = None
