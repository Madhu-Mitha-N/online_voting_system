from flask import request, jsonify
from flask import session

from services.admin_service import (
    add_admin_service,
    get_admins_service,
    get_single_admin_service,
    update_admin_service,
    delete_admin_service,
    admin_login_service
)


# CREATE ADMIN
def create_admin_controller():
    data = request.get_json()

    admin_name = data.get("admin_name")
    password = data.get("password")

    if not admin_name or not password:
        return jsonify({
            "error": "admin_name and password required"
        }), 400

    add_admin_service(admin_name, password)

    return jsonify({
        "message": "Admin created successfully"
    }), 201


# ADMN LOGIN 

def admin_login_controller():

    data = request.get_json()

    admin_name = data.get("admin_name")
    password = data.get("password")

    admin = admin_login_service(
        admin_name,
        password
    )

    if not admin:

        return jsonify({
            "error": "Invalid admin credentials"
        }), 401
    # AFTER SUCCESS LOGIN
    session["admin_id"] = admin["id"]
    session["admin_name"] = admin["admin_name"]

    return jsonify({
        "message": "Login successful",

        "admin": {
            "id": admin["id"],
            "admin_name": admin["admin_name"]
        }

    }), 200

# GET ALL ADMINS
def get_all_admins_controller():
    admins = get_admins_service()

    admin_list = []

    for admin in admins:
        admin_list.append({
            "id": admin["id"],
            "admin_name": admin["admin_name"]
        })

    return jsonify(admin_list), 200


# GET SINGLE ADMIN
def get_single_admin_controller(admin_id):
    admin = get_single_admin_service(admin_id)

    if not admin:
        return jsonify({
            "error": "Admin not found"
        }), 404

    return jsonify({
        "id": admin["id"],
        "admin_name": admin["admin_name"]
    }), 200


# UPDATE ADMIN
def update_admin_controller(admin_id):
    data = request.get_json()

    admin_name = data.get("admin_name")
    password = data.get("password")

    update_admin_service(admin_id, admin_name, password)

    return jsonify({
        "message": "Admin updated successfully"
    }), 200


# DELETE ADMIN
def delete_admin_controller(admin_id):
    delete_admin_service(admin_id)

    return jsonify({
        "message": "Admin deleted successfully"
    }), 200


