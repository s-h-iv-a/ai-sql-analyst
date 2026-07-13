import re

from openai import OpenAI

from app.core.config import settings
from app.prompts.sql_prompt import EXPLANATION_PROMPT, SCHEMA_CONTEXT, SQL_GENERATION_PROMPT


class LLMService:
    def __init__(self):
        self.client = OpenAI(api_key=settings.openai_api_key)
        self.model = settings.openai_model

    def generate_sql(self, question: str) -> str:
        prompt = SQL_GENERATION_PROMPT.format(
            schema=SCHEMA_CONTEXT,
            question=question,
        )
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            temperature=0,
        )
        sql = response.choices[0].message.content.strip()
        return self._strip_markdown(sql)

    def explain_results(self, question: str, sql: str, results: list[dict]) -> str:
        prompt = EXPLANATION_PROMPT.format(
            question=question,
            sql=sql,
            results=results,
        )
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            temperature=0.3,
        )
        return response.choices[0].message.content.strip()

    @staticmethod
    def _strip_markdown(sql: str) -> str:
        sql = sql.strip()
        if sql.startswith("```"):
            sql = re.sub(r"^```(?:sql)?\n?", "", sql)
            sql = re.sub(r"\n?```$", "", sql)
        return sql.strip()
