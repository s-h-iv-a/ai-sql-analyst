import re

FORBIDDEN_KEYWORDS = (
    "INSERT",
    "UPDATE",
    "DELETE",
    "DROP",
    "ALTER",
    "CREATE",
    "TRUNCATE",
    "REPLACE",
    "ATTACH",
    "DETACH",
    "PRAGMA",
)


def validate_sql(sql: str) -> str:
    cleaned = sql.strip().rstrip(";")
    upper = cleaned.upper()

    if not upper.startswith("SELECT"):
        raise ValueError("Only SELECT queries are allowed.")

    for keyword in FORBIDDEN_KEYWORDS:
        if re.search(rf"\b{keyword}\b", upper):
            raise ValueError(f"Forbidden SQL keyword detected: {keyword}")

    if ";" in cleaned:
        raise ValueError("Multiple SQL statements are not allowed.")

    return cleaned
