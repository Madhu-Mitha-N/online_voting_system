from flask import Blueprint

from controllers.voter_controller import (
    create_voter_controller,
    get_all_voters_controller,
    get_single_voter_controller,
    update_voter_controller,
    delete_voter_controller,
    update_voter_profile_controller,
    voter_login_controller,
    change_password_controller,
    profile_password_change_controller
)

voter_bp = Blueprint("voter_bp", __name__)


# CREATE VOTER
@voter_bp.route("/voter/create", methods=["POST"])
def create_voter_route():
    return create_voter_controller()


# GET ALL VOTERS
@voter_bp.route("/voter/all", methods=["GET"])
def get_all_voters_route():
    return get_all_voters_controller()


# GET SINGLE VOTER
@voter_bp.route("/voter/<int:voter_id>", methods=["GET"])
def get_single_voter_route(voter_id):
    return get_single_voter_controller(voter_id)


# UPDATE VOTER
@voter_bp.route("/voter/update/<int:voter_id>", methods=["PUT"])
def update_voter_route(voter_id):
    return update_voter_controller(voter_id)


# DELETE VOTER
@voter_bp.route("/voter/delete/<int:voter_id>", methods=["DELETE"])
def delete_voter_route(voter_id):
    return delete_voter_controller(voter_id)


# LOGIN
@voter_bp.route("/voter/login", methods=["POST"])
def voter_login_route():
    return voter_login_controller()


# CHANGE PASSWORD
@voter_bp.route("/voter/change-password/<int:voter_id>", methods=["PUT"])
def change_password_route(voter_id):
    return change_password_controller(voter_id)

# UPDATE PROFILE
@voter_bp.route(
    "/voter/profile/update/<int:voter_id>",
    methods=["PUT"]
)
def update_profile(voter_id):

    return update_voter_profile_controller(
        voter_id
    )

# PROFILE PASSWORD CHANGE
@voter_bp.route(
    "/voter/profile-change-password/<int:voter_id>",
    methods=["PUT"]
)
def profile_password_change_route(voter_id):
    return profile_password_change_controller(voter_id)