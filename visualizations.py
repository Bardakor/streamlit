import plotly.express as px
import plotly.graph_objects as go
from queries import *
from utils import run_query

# 1. Donut Chart for Top Ports


def top_ports_donut_chart():
    data = run_query(top_ports_query())
    fig = go.Figure(go.Pie(
        labels=data['port_name'],
        values=data['usage_count'],
        hole=0.4,
        pull=[0.1] * len(data),  # Pulls out each segment slightly
        textinfo="label+percent",
        insidetextorientation="radial"
    ))
    fig.update_traces(rotation=90, direction="clockwise",
                      marker=dict(line=dict(color="black", width=2)))
    fig.update_layout(title="Top 10 Ports by Usage", template="plotly_dark")
    return fig

# 2. Bar Chart for Vessel Distribution


def vessel_distribution_chart():
    data = run_query(vessel_distribution_query())
    fig = px.bar(data, x='vessel_type', y='count',
                 title="Distribution of Vessel Types", template="plotly_dark")
    fig.update_layout(xaxis_tickangle=-45)
    return fig

# 3. Interactive Map of Voyages


def voyage_map():
    # Placeholder for a detailed map, using sample lat/lon data if available
    fig = go.Figure()  # Use Folium or Plotly for maps based on real voyage start and end data
    return fig

# 4. Box Plot for Voyage Durations


def voyage_durations_boxplot():
    data = run_query(voyage_durations_query())
    fig = px.box(data, y="duration_days",
                 title="Voyage Duration Distribution", template="plotly_dark")
    return fig

# 5. Timeline for User Activity


def user_activity_timeline():
    data = run_query(
        "SELECT issuer_id AS user_id, created_at FROM api_voyage;")
    fig = px.scatter(data, x="created_at", y="user_id",
                     title="User Activity Timeline", template="plotly_dark")
    return fig


# 6. Cross-Data Analysis: Advanced Correlation Insights


def cross_data_analysis():
    data = run_query("""
    SELECT 
        s.vessel_type,
        AVG(julianday(v.eta) - julianday(v.etd)) AS avg_duration,
        COUNT(l.voyage_id) AS port_visits
    FROM api_voyage v
    JOIN api_leg l ON v.voyage_id = l.voyage_id
    JOIN api_ship s ON l.captain_id = s.captain_id
    GROUP BY s.vessel_type
    """)
    fig = px.scatter(data, x="vessel_type", y="avg_duration", size="port_visits", color="vessel_type",
                     title="Average Duration and Port Visits by Vessel Type", template="plotly_dark")
    return fig
