from flask import request, jsonify

from services.voter_service import (
    create_voter_service,
    get_all_voters_service,
    get_single_voter_service,
    update_voter_service,
    delete_voter_service,
    voter_login_service,
    change_password_service,
    verify_voter_password_service,
    update_profile_service
)
# from services.voter_service import (
#     verify_voter_password_service,
#     update_profile_service
# )
# from models.voter_model import (
#     verify_voter_password,
#     update_voter_profile,
#     verify_voter_password,
#     change_voter_password
# )


# CREATE VOTER
def create_voter_controller():

    data = request.get_json()
    if not data.get("name"):
        return jsonify({
        "error": "Name is required"
        }), 400

    voter_id = data.get("voter_id")

    default_password = f"Vote@{voter_id}"

    voter_data = {
        "voter_id": voter_id,
        "name": data.get("name"),
        "phone": data.get("phone"),
        "dob": data.get("dob"),
        "district": data.get("district"),
        "ward": data.get("ward"),
        "email": data.get("email"),
        "password": default_password
    }

    try:

        create_voter_service(voter_data)

        return jsonify({
            "message": "Voter registered successfully",
            "default_password": default_password
        }), 201

    except Exception as e:

        return jsonify({
            "error": str(e)
        }), 400


# GET ALL VOTERS
def get_all_voters_controller():

    voters = get_all_voters_service()

    voter_list = []

    for voter in voters:
        voter_list.append({
            "voter_id": voter["voter_id"],
            "name": voter["name"],
            "phone": voter["phone"],
            "district": voter["district"],
            "ward": voter["ward"],
            "email": voter["email"],
            "has_voted": voter["has_voted"]
        })

    return jsonify(voter_list), 200


# GET SINGLE VOTER
def get_single_voter_controller(voter_id):

    voter = get_single_voter_service(voter_id)

    if not voter:
        return jsonify({
            "error": "Voter not found"
        }), 404

    return jsonify({
        "voter_id": voter["voter_id"],
        "name": voter["name"],
        "phone": voter["phone"],
        "dob": voter["dob"],
        "district": voter["district"],
        "ward": voter["ward"],
        "email": voter["email"],
        "has_voted": voter["has_voted"]
    }), 200


# UPDATE VOTER
def update_voter_controller(voter_id):

    data = request.get_json()

    update_voter_service(voter_id, data)

    return jsonify({
        "message": "Voter updated successfully"
    }), 200


# DELETE VOTER
def delete_voter_controller(voter_id):

    delete_voter_service(voter_id)

    return jsonify({
        "message": "Voter deleted successfully"
    }), 200


# LOGIN
def voter_login_controller():

    data = request.get_json()

    voter_id = data.get("voter_id")
    password = data.get("password")

    voter = voter_login_service(voter_id, password)

    if not voter:
        return jsonify({
            "error": "Invalid credentials"
        }), 401

    return jsonify({
    "message": "Login successful",
    "voter": {
        "voter_id": voter["voter_id"],
        "name": voter["name"],
        "is_default_password": voter["is_default_password"],
        "has_voted": voter["has_voted"]
    },
    "force_password_change": voter["is_default_password"] == 1
}), 200


# CHANGE PASSWORD
def change_password_controller(voter_id):

    data = request.get_json()
    new_password = data.get("new_password")

    if not new_password:
        return jsonify({"error": "New password required"}), 400

    success = change_password_service(voter_id, new_password)

    if not success:
        return jsonify({"error": "Weak password"}), 400

    return jsonify({
        "message": "Password changed successfully"
    }), 200
    
# UPDATE PROFILE
def update_voter_profile_controller(voter_id):

    data = request.get_json()

    update_profile_service(voter_id, data)

    return jsonify({
        "message":
        "Profile updated successfully"
    }), 200

# PROFILE PASSWORD CHANGE
def profile_password_change_controller(voter_id):

    data = request.get_json()

    current_password = data.get("current_password")
    new_password = data.get("new_password")

    voter = verify_voter_password_service(
        voter_id,
        current_password
    )

    if not voter:
        return jsonify({
            "error": "Current password incorrect"
        }), 400

    success = change_password_service(
        voter_id,
        new_password
    )

    if not success:
        return jsonify({
            "error": "Weak password"
        }), 400

    return jsonify({
        "message": "Password updated successfully"
    }), 200