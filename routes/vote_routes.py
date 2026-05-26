from flask import Blueprint

from controllers.vote_controller import (
    vote_controller,
    get_all_votes_controller
)

vote_bp = Blueprint("vote_bp", __name__)


# SUBMIT VOTE
@vote_bp.route("/vote", methods=["POST"])
def vote():
    return vote_controller()


# GET ALL VOTES
@vote_bp.route("/vote/all", methods=["GET"])
def get_all_votes():
    return get_all_votes_controller()