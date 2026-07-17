from sqlalchemy import inspect
from app.database.database import engine


def load_schema():

    inspector = inspect(engine)

    schema = ""

    tables = inspector.get_table_names()

    for table in tables:

        schema += f"\nTable: {table}\n"

        columns = inspector.get_columns(table)

        for column in columns:

            schema += f" - {column['name']} ({column['type']})\n"

    return schema