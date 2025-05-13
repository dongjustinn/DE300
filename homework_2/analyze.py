import duckdb
import pandas as pd
import os

con = duckdb.connect("mimic.db")

csv_dir = 'data'
for fname in os.listdir(csv_dir):
    if fname.endswith('.csv'):
        table_name = fname.replace('.csv', '').lower()
        full_path = os.path.join(csv_dir, fname)
        con.execute(f"CREATE OR REPLACE TABLE {table_name} AS SELECT * FROM read_csv_auto('{full_path}')")

result = con.execute("SELECT COUNT(*) AS admission_count FROM admissions").fetchdf()

result.to_csv("output/admission_count.csv", index=False)
