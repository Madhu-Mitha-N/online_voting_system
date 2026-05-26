from flask import Blueprint
from controllers.admin_dashboard_controller import *

dashboard_bp = Blueprint("dashboard_bp", __name__)


# TOTAL STATS
@dashboard_bp.route("/admin/dashboard/stats", methods=["GET"])
def stats():
    return dashboard_stats_controller()


# CANDIDATE RANKING
@dashboard_bp.route("/admin/dashboard/ranking", methods=["GET"])
def ranking():
    return ranking_controller()