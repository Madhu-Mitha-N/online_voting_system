from flask import jsonify
from services.admin_dashboard_service import (
    get_dashboard_stats,
    get_ranking_service
)


# DASHBOARD SUMMARY
def dashboard_stats_controller():

    data = get_dashboard_stats()

    return jsonify({
        "message": "Dashboard stats fetched successfully",
        "data": data
    }), 200


# RANKING
def ranking_controller():

    data = get_ranking_service()

    return jsonify({
        "message": "Candidate ranking fetched successfully",
        "ranking": data
    }), 200