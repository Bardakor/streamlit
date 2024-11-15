import psycopg2
from contextlib import contextmanager

# PostgreSQL connection configuration
config = {
    "host": "34.159.114.196",
    "port": "5432",
    "database": "django-amphitrite",
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
