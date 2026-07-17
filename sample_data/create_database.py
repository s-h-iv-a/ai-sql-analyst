import sqlite3
import pandas as pd
import os


BASE_DIR = os.path.dirname(__file__)

DB_PATH = os.path.join(
    BASE_DIR,
    "../backend/sample.db"
)


def create_database():

    connection = sqlite3.connect(DB_PATH)


    files = {
        "customers": "customers.csv",
        "products": "products.csv",
        "sales": "sales.csv"
    }


    for table, file in files.items():

        path = os.path.join(
            BASE_DIR,
            file
        )

        df = pd.read_csv(path)

        df.to_sql(
            table,
            connection,
            if_exists="replace",
            index=False
        )

        print(
            f"Created table: {table}"
        )


    connection.close()

    print(
        "Database created successfully"
    )


if __name__ == "__main__":
    create_database()