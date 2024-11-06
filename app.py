import streamlit as st
from visualizations import *
from utils import run_query
import time

# Set wide page configuration with a background color
st.set_page_config(
    page_title="Comprehensive Maritime Dashboard",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for styling
st.markdown(
    '''
    <style>
    body {
        background-color: #f0f2f5; /* Light background color */
    }
    .header {
        text-align: center;
        font-size: 2.5em;
        color: #2a7ae2; /* Title color */
        margin-bottom: 20px;
    }
    .metric {
        font-size: 20px !important;
        font-weight: bold;
        color: #4CAF50; /* Metric color */
    }
    .subheader {
        color: #2a7ae2; /* Subheader color */
    }
    .sidebar .sidebar-content {
        background-color: #ffffff; /* Sidebar background */
    }
    </style>
    ''', unsafe_allow_html=True
)

# Centered title
st.markdown('<h1 class="header">🚢 Maritime Insights Dashboard</h1>',
            unsafe_allow_html=True)

# Sidebar options
st.sidebar.title("Dashboard Options")
st.sidebar.markdown("Choose filters or preferences here.")

# Key Maritime Metrics
st.markdown("### 🌍 Key Maritime Metrics")
with st.spinner("Loading Summary Metrics..."):
    time.sleep(1)
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Total Voyages", run_query(
        "SELECT COUNT(*) FROM api_voyage")['COUNT(*)'][0])
    col2.metric("Unique Ports", run_query(
        "SELECT COUNT(DISTINCT port_name) FROM api_port")['COUNT(DISTINCT port_name)'][0])
    col3.metric("Vessel Types", run_query(
        "SELECT COUNT(DISTINCT vessel_type) FROM api_ship")['COUNT(DISTINCT vessel_type)'][0])
    col4.metric("Active Users", run_query(
        "SELECT COUNT(DISTINCT id) AS count FROM auth_user")['count'][0])

# Port and Vessel Insights
st.markdown("### 🌐 Port and Vessel Insights")
col1, col2 = st.columns([2, 2])

with col1:
    st.subheader("Top 10 Ports by Usage")
    with st.spinner("Loading Top Ports..."):
        st.plotly_chart(top_ports_donut_chart(), use_container_width=True)

with col2:
    st.subheader("Vessel Distribution")
    with st.spinner("Loading Vessel Distribution..."):
        st.plotly_chart(vessel_distribution_chart(), use_container_width=True)

# Voyage Analysis
st.markdown("### 🌊 Voyage Analysis")
col1, col2 = st.columns([3, 1])

with col1:
    st.subheader("Interactive Voyage Map")
    with st.spinner("Loading Voyage Map..."):
        st.plotly_chart(voyage_map(), use_container_width=True)

with col2:
    st.subheader("Voyage Durations Distribution")
    with st.spinner("Loading Voyage Durations..."):
        st.plotly_chart(voyage_durations_boxplot(), use_container_width=True)

# User Activity and Cross-Data Insights
st.markdown("### 📊 User Activity and Cross-Data Insights")
col1, col2 = st.columns([1.5, 2.5])

with col1:
    st.subheader("User Activity Timeline")
    with st.spinner("Loading User Activity..."):
        st.plotly_chart(user_activity_timeline(), use_container_width=True)

with col2:
    st.subheader("Cross-Data Insights")
    with st.spinner("Generating Cross-Data Analysis..."):
        st.plotly_chart(cross_data_analysis(), use_container_width=True)

# Analysis Overview
st.markdown("#### 🔍 Analysis Overview")
st.write("""This dashboard provides a comprehensive view of maritime operations by integrating multiple data sources.""")
