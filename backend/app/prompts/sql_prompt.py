SCHEMA_CONTEXT = """
Tables:

products(product_id, name, category, price)
customers(customer_id, name, email, country)
sales(sale_id, product_id, customer_id, quantity, sale_date, total_amount)

Relationships:
- sales.product_id -> products.product_id
- sales.customer_id -> customers.customer_id
"""

SQL_GENERATION_PROMPT = """
You are a SQL expert. Given a SQLite database schema and a user question,
write a single SELECT query that answers the question.

Rules:
- Return only the SQL query, no markdown or explanation
- Use only SELECT statements
- Use table and column names exactly as provided
- Join tables when needed

Schema:
{schema}

Question:
{question}
"""

EXPLANATION_PROMPT = """
You are a data analyst. Explain the following SQL query results in plain English.

Question: {question}
SQL: {sql}
Results (JSON): {results}

Provide a concise, helpful explanation for a business user.
"""
