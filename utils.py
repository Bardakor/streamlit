import streamlit as st
import pandas as pd
from database import get_connection


def run_query(query):
    """Run a SQL query and return the results as a Pandas DataFrame."""
    conn = get_connection()
    return pd.read_sql_query(query, conn)


# Streamlit app
st.title("Cloud SQL Proxy Demo")

try:
    # Example query
    data = run_query("SELECT * FROM api_voyage LIMIT 10;")
    st.write(data)
except Exception as e:
    st.error(f"Error: {e}")
