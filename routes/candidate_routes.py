from flask import Blueprint
from controllers.candidate_controller import *

candidate_bp = Blueprint("candidate_bp", __name__)


# CREATE
@candidate_bp.route("/candidate/create", methods=["POST"])
def create():
    return create_candidate_controller()


# GET ALL (FOR VOTING UI)
@candidate_bp.route("/candidate/all", methods=["GET"])
def get_all():
    return get_all_candidates_controller()


# GET ONE
@candidate_bp.route("/candidate/<int:candidate_id>", methods=["GET"])
def get_one(candidate_id):
    return get_single_candidate_controller(candidate_id)


# UPDATE
@candidate_bp.route("/candidate/update/<int:candidate_id>", methods=["PUT"])
def update(candidate_id):
    return update_candidate_controller(candidate_id)


# DELETE
@candidate_bp.route("/candidate/delete/<int:candidate_id>", methods=["DELETE"])
def delete(candidate_id):
    return delete_candidate_controller(candidate_id)

