import psycopg2
from contextlib import contextmanager

# PostgreSQL connection configuration
config = {
    "host": "/cloudsql/aiceanographers:europe-west3:django-amphitrite",
    "port": "5432",
    "database": "django-bulletin",
    "user": "compare",
    "password": "easy"
}


@contextmanager
def get_connection():
    """Context manager for PostgreSQL database connection, to ensure it closes automatically."""
    conn = psycopg2.connect(**config)
    try:
        yield conn
    finally:
        conn.close()
