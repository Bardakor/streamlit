import database as db
from utils import run_query


# Top Ports Query
def top_ports_query():
    return """
    SELECT p.port_name, COUNT(f.favorite_port_id) AS usage_count
    FROM api_favoriteport f
    JOIN api_port p ON f.favorite_port_id = p.id
    GROUP BY p.port_name
    ORDER BY usage_count DESC
    LIMIT 10
    """

# Vessel Distribution Query


def vessel_distribution_query():
    return """
    SELECT vessel_type, COUNT(*) AS count
    FROM api_ship
    GROUP BY vessel_type
    ORDER BY count DESC
    """

# Voyage Durations Query


def voyage_durations_query():
    return """
    SELECT (eta - etd) AS duration_days
    FROM api_voyage
    WHERE eta IS NOT NULL AND etd IS NOT NULL
    """


# def user_activity_timeline_query():
#     """
#     Returns the SQL query to get user activity timeline data.
#     Fetches the user_id and creation date of each voyage for timeline analysis.
#     """
#     query = """
#     SELECT user_id, created_at
#     FROM api_voyage
#     """
#     return query


# def cross_data_analysis_query():
#     query = """
#     SELECT 
#         s.vessel_type,
#         AVG(julianday(v.eta) - julianday(v.etd)) AS avg_duration,
#         COUNT(l.voyage_id) AS port_visits
#     FROM api_voyage v
#     JOIN api_leg l ON v.voyage_id = l.voyage_id
#     JOIN api_ship s ON l.vessel_id = s.id  -- Use the correct vessel ID column here
#     GROUP BY s.vessel_type
#     """
#     return query


# Utility function to run each query (optional, based on how `database.py` is implemented)
def execute_query(query):
    """
    Executes a query using the run_query function from the database module.
    """
    return db.run_query(query)
