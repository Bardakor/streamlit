# utils.py

import sqlite3
import pandas as pd
from contextlib import contextmanager

DB_PATH = 'my_database.sqlite3'

@contextmanager
def get_connection():
    conn = sqlite3.connect(DB_PATH)
    try:
        yield conn
    finally:
        conn.close()

def run_query(query: str):
    with get_connection() as conn:
        return pd.read_sql_query(query, conn)
