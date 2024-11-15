import pandas as pd
from database import get_connection
import streamlit as st

def run_query(query):
    """Execute a query and return the results as a DataFrame."""
    try:
        with get_connection() as conn:
            return pd.read_sql_query(query, conn)
    except Exception as e:
        st.error(f"Error executing query: {e}")
        return pd.DataFrame()  # Return an empty DataFrame on error
