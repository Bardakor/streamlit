import os
from google.cloud.sql.connector import Connector
import pg8000.native  # Cloud SQL-compatible Python driver


def get_connection():
    """Establish a secure connection to the PostgreSQL database using Cloud SQL Connector."""
    # Create a Cloud SQL Connector instance
    connector = Connector()

    # Replace with your Google Cloud SQL instance details
    instance_connection_name = "your-project-id:your-region:your-instance-name"

    # Get the connection using the Connector
    conn = connector.connect(
        instance_connection_name,
        "pg8000",
        user="compare",
        password="easy",
        db="django-bulletin",
    )

    return conn
