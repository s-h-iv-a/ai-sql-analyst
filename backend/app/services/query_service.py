from sqlalchemy import text

from app.database.database import engine
from app.database.schema_loader import load_schema

from app.prompts.sql_prompt import (
    SQL_SYSTEM_PROMPT,
    EXPLANATION_PROMPT
)

from app.llm.groq_client import (
    generate_sql,
    generate_explanation
)
from app.utils.validator import validate_sql

from app.utils.chart_builder import build_chart



def execute_query(question: str):


    schema = load_schema()


    prompt = SQL_SYSTEM_PROMPT.format(
        schema=schema
    )


    sql_prompt = f"""
{prompt}

User question:

{question}
"""


    sql = generate_sql(
        sql_prompt
    )


    sql = sql.replace(
        "```sql",
        ""
    ).replace(
        "```",
        ""
    ).strip()



    validate_sql(sql)



    with engine.connect() as connection:

        result = connection.execute(
            text(sql)
        )


        rows = [

            dict(row._mapping)

            for row in result.fetchall()

        ]



    explanation_prompt = EXPLANATION_PROMPT.format(

        question=question,

        sql=sql,

        results=rows

    )


    explanation = generate_explanation(
        explanation_prompt
    )



    chart = build_chart(
        rows
    )


    return {

        "sql": sql,

        "results": rows,

        "explanation": explanation,

        "chart": chart

    }