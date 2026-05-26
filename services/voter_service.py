import re

from models.voter_model import (
    create_voter,
    get_all_voters,
    get_voter_by_id,
    update_voter,
    delete_voter,
    voter_login,
    change_voter_password,
    verify_voter_password
)


# CREATE VOTER
def create_voter_service(voter_data):
    create_voter(voter_data)


# GET ALL
def get_all_voters_service():
    return get_all_voters()


# GET SINGLE
def get_single_voter_service(voter_id):
    return get_voter_by_id(voter_id)


# UPDATE
def update_voter_service(voter_id, voter_data):
    update_voter(voter_id, voter_data)


# DELETE
def delete_voter_service(voter_id):
    delete_voter(voter_id)


# LOGIN
def voter_login_service(voter_id, password):
    return voter_login(voter_id, password)


# CHANGE PASSWORD
def change_password_service(voter_id, new_password):

    if not validate_password(new_password):
        return False

    change_voter_password(voter_id, new_password)
    return True

# =========================
# PASSWORD VALIDATION
# =========================
def validate_password(password):

    if len(password) < 8:
        return False

    if not re.search(r"[A-Z]", password):
        return False

    if not re.search(r"[a-z]", password):
        return False

    if not re.search(r"[0-9]", password):
        return False

    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        return False

    return True


def verify_voter_password_service(voter_id, password):

    return verify_voter_password(voter_id, password)

def update_profile_service(voter_id, data):
    from models.voter_model import update_voter_profile
    update_voter_profile(voter_id, data)