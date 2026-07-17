import re


FORBIDDEN_KEYWORDS = [

    "DROP",
    "DELETE",
    "UPDATE",
    "INSERT",
    "ALTER",
    "CREATE",
    "TRUNCATE"

]


def validate_sql(sql: str):

    sql_upper = sql.upper()


    for keyword in FORBIDDEN_KEYWORDS:

        if re.search(
            rf"\b{keyword}\b",
            sql_upper
        ):

            raise ValueError(
                f"Unsafe SQL detected: {keyword}"
            )


    if not sql_upper.strip().startswith("SELECT"):

        raise ValueError(
            "Only SELECT queries are allowed"
        )


    return True
