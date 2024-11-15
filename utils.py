import streamlit as st
import pandas as pd
from database import get_connection


def run_query(query):
    """Run a SQL query and return the results as a Pandas DataFrame."""
    conn = get_connection()
    return pd.read_sql_query(query, conn)


