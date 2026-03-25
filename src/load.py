from pathlib import Path
import pandas as pd
from sqlalchemy import create_engine, text


def get_engine():
    return create_engine("sqlite:///credit_risk_dw.db", future=True)


def create_tables(engine):
    sql_path = Path("sql/create_tables.sql")
    sql_script = sql_path.read_text(encoding="utf-8")

    with engine.begin() as conn:
        for statement in sql_script.split(";"):
            statement = statement.strip()
            if statement:
                conn.execute(text(statement))


def load_csvs(engine):
    df_convenios = pd.read_csv("data/raw/convenios.csv")
    df_creditos = pd.read_csv("data/raw/creditos.csv")
    df_pagos = pd.read_csv("data/raw/pagos.csv")

    df_convenios.to_sql("convenios", con=engine, if_exists="replace", index=False)
    df_creditos.to_sql("creditos", con=engine, if_exists="replace", index=False)
    df_pagos.to_sql("pagos", con=engine, if_exists="replace", index=False)


if __name__ == "__main__":
    engine = get_engine()
    create_tables(engine)
    load_csvs(engine)
    print("Tablas creadas y datos cargados correctamente.")