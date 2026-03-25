from pathlib import Path
from sqlalchemy import create_engine, text

engine = create_engine("sqlite:///credit_risk_dw.db", future=True)

sql_path = Path("sql/business_queries.sql")
sql_script = sql_path.read_text(encoding="utf-8")

queries = [q.strip() for q in sql_script.split(";") if q.strip()]

with engine.connect() as conn:
    for i, query in enumerate(queries, start=1):
        print(f"\n--- Query {i} ---")
        result = conn.execute(text(query))
        rows = result.fetchall()

        for row in rows[:10]:
            print(row)

        if len(rows) > 10:
            print(f"... {len(rows)} filas en total")