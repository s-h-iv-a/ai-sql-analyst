import pandas as pd
from sqlalchemy import text

from app.database.database import engine
from app.llm.generator import LLMService
from app.models.query_log import QueryLog
from app.utils.chart_builder import build_chart
from app.utils.sql_validator import validate_sql


class QueryService:
    def __init__(self):
        self.llm = LLMService()

    def run(self, question: str, db_session) -> dict:
        generated_sql = self.llm.generate_sql(question)
        safe_sql = validate_sql(generated_sql)

        with engine.connect() as connection:
            rows = connection.execute(text(safe_sql)).mappings().all()

        results = [dict(row) for row in rows]
        explanation = self.llm.explain_results(question, safe_sql, results)
        chart = build_chart(results)

        log = QueryLog(natural_language=question, generated_sql=safe_sql)
        db_session.add(log)
        db_session.commit()

        return {
            "question": question,
            "sql": safe_sql,
            "results": results,
            "row_count": len(results),
            "explanation": explanation,
            "chart": chart,
        }
