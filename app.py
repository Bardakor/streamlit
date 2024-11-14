import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from PIL import Image
from visualizations import *
from utils import run_query
import time

import subprocess
import sys


def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])


try:
    import plotly.express as px
except ImportError:
    install("plotly")

# Set wide page configuration and favicon
st.set_page_config(
    page_title="Comprehensive Maritime Dashboard",
    layout="wide",
    page_icon="🚢"
)

# Load an icon or background image (optional)
# logo = Image.open("path_to_logo.png")
# st.image(logo, width=100)  # Display logo if available

# Custom CSS for global styling with a black, white, and gray tone
st.markdown(
    '''
    <style>
    /* Load Google Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;700&display=swap');
    
    /* Background & Fonts */
    body {
        font-family: 'Roboto', sans-serif;
        background-color: #121212;
        color: #e0e0e0;
    }

    /* Titles */
    .title {
        text-align: center;
        font-size: 2.8em;
        color: #ffffff;
        margin-top: 20px;
        font-weight: 700;
    }

    .section-header {
        font-size: 2.2em;
        text-align: center;
        color: #b0b0b0;
        margin-top: 20px;
        font-weight: 400;
    }

    /* Metric styling */
    .stMetric {
        background-color: #222222;
        border-radius: 12px;
        padding: 20px;
        color: #ffffff;
        font-size: 1.1em;
        box-shadow: 0px 8px 16px rgba(0, 0, 0, 0.4);
        transition: transform 0.2s ease, background-color 0.2s ease;
    }
    .stMetric:hover {
        transform: scale(1.04);
        background-color: #333333;
    }

    /* Button styling */
    .stButton>button {
        background-color: #ffffff;
        color: #333333;
        border: none;
        border-radius: 10px;
        padding: 10px 25px;
        font-weight: 600;
        transition: background-color 0.3s ease;
    }
    .stButton>button:hover {
        background-color: #444444;
        color: #ffffff;
    }

    /* Flexbox for center alignment */
    .flex-center {
        display: flex;
        justify-content: center;
        align-items: center;
    }

    /* Footer */
    footer {
        text-align: center;
        padding: 20px;
        color: #a6a6a6;
        font-size: 1em;
        margin-top: 40px;
    }
    
    /* Improved scrollbar design */
    ::-webkit-scrollbar {
        width: 8px;
    }
    ::-webkit-scrollbar-track {
        background: #121212;
    }
    ::-webkit-scrollbar-thumb {
        background-color: #444444;
        border-radius: 10px;
    }
    </style>
    ''', unsafe_allow_html=True
)

# Centered main title with subtle shadow effect
st.markdown('<h1 class="title">🚢 Maritime Insights Dashboard</h1>',
            unsafe_allow_html=True)

# Key Maritime Metrics in a flex layout
st.markdown('<h2 class="section-header">🌍 Key Maritime Metrics</h2>',
            unsafe_allow_html=True)
with st.spinner("Loading Summary Metrics..."):
    time.sleep(1)
    metrics_container = st.container()
    with metrics_container:
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
st.markdown('<h2 class="section-header">🌐 Port and Vessel Insights</h2>',
            unsafe_allow_html=True)
with st.spinner("Loading Visual Insights..."):
    time.sleep(1)
    insight_container = st.container()
    with insight_container:
        col1, col2 = st.columns([1, 1])

        with col1:
            st.markdown(
                '<h3 class="subsection-title">Top 10 Ports by Usage</h3>', unsafe_allow_html=True)
            st.plotly_chart(top_ports_donut_chart(), use_container_width=True)

        with col2:
            st.markdown(
                '<h3 class="subsection-title">Vessel Distribution</h3>', unsafe_allow_html=True)
            st.plotly_chart(vessel_distribution_chart(),
                            use_container_width=True)

# Voyage Analysis Section
st.markdown('<h2 class="section-header">🌊 Voyage Analysis</h2>',
            unsafe_allow_html=True)
with st.spinner("Loading Voyage Data..."):
    time.sleep(1)
    voyage_container = st.container()
    with voyage_container:
        col1, col2 = st.columns([3, 1])

        with col1:
            st.markdown(
                '<h3 class="subsection-title">Interactive Voyage Map</h3>', unsafe_allow_html=True)
            st.plotly_chart(voyage_map(), use_container_width=True)

        with col2:
            st.markdown(
                '<h3 class="subsection-title">Voyage Durations Distribution</h3>', unsafe_allow_html=True)
            st.plotly_chart(voyage_durations_boxplot(),
                            use_container_width=True)

# Analysis Overview with custom styling
st.markdown('<h2 class="section-header">🔍 Analysis Overview</h2>',
            unsafe_allow_html=True)
st.write("""
This dashboard provides an in-depth exploration of maritime operations, utilizing data from multiple sources to reveal patterns and insights into port usage, vessel distribution, and voyage characteristics. Users can explore metrics and visual insights that are essential for strategic maritime decisions.
""")

# Footer with minimal styling and consistent font
st.markdown('<footer>© 2024 Maritime Insights</footer>',
            unsafe_allow_html=True)
