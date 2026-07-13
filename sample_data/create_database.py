from pathlib import Path

import pandas as pd
from sqlalchemy import create_engine

DATA_DIR = Path(__file__).resolve().parent
DB_PATH = DATA_DIR / "sales.db"


def create_database():
    engine = create_engine(f"sqlite:///{DB_PATH}")

    tables = {
        "products": "products.csv",
        "customers": "customers.csv",
        "sales": "sales.csv",
    }

    for table_name, filename in tables.items():
        df = pd.read_csv(DATA_DIR / filename)
        df.to_sql(table_name, engine, if_exists="replace", index=False)

    print(f"Database created at {DB_PATH}")


if __name__ == "__main__":
    create_database()
