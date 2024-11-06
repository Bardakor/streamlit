# database.py

import sqlite3
from contextlib import contextmanager

DB_PATH = 'my_database.sqlite3'


@contextmanager
def get_connection():
    """Context manager for database connection, to ensure it closes automatically."""
    conn = sqlite3.connect(DB_PATH)
    try:
        yield conn
    finally:
        conn.close()
