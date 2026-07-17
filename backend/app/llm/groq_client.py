import os
from groq import Groq

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)


MODEL = "llama-3.3-70b-versatile"


def generate_sql(question, schema=None):
    prompt = f"""
You are an expert SQL developer.

Database schema:
{schema if schema else "No schema provided"}

Convert this user request into SQL.

User request:
{question}

Return only SQL.
"""

    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0
    )

    return response.choices[0].message.content


def generate_explanation(sql, result=None):
    prompt = f"""
Explain this SQL query in simple language.

SQL:
{sql}

Result:
{result if result else "No result data provided"}
"""

    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.3
    )

    return response.choices[0].message.content