from flask import Blueprint, render_template
from flask import session, redirect 

from controllers.admin_controller import (
    create_admin_controller,
    get_all_admins_controller,
    get_single_admin_controller,
    update_admin_controller,
    delete_admin_controller,
    admin_login_controller
)

admin_bp = Blueprint("admin_bp", __name__)

@admin_bp.route("/admin/dashboard")
def admin_dashboard():

    if "admin_id" not in session:
        return redirect("/admin/login-page")

    return render_template("admin/admin_dashboard.html")

# CREATE ADMIN
@admin_bp.route("/admin/create", methods=["POST"])
def create_admin_route():
    return create_admin_controller()


# GET ALL ADMINS
@admin_bp.route("/admin/all", methods=["GET"])
def get_all_admins_route():
    return get_all_admins_controller()


# GET SINGLE ADMIN
@admin_bp.route("/admin/<int:admin_id>", methods=["GET"])
def get_single_admin_route(admin_id):
    return get_single_admin_controller(admin_id)


# UPDATE ADMIN
@admin_bp.route("/admin/update/<int:admin_id>", methods=["PUT"])
def update_admin_route(admin_id):
    return update_admin_controller(admin_id)


# DELETE ADMIN
@admin_bp.route("/admin/delete/<int:admin_id>", methods=["DELETE"])
def delete_admin_route(admin_id):
    return delete_admin_controller(admin_id)


# ADMIN LOGIN
@admin_bp.route("/admin/login", methods=["POST"])
def admin_login_route():
    return admin_login_controller()

@admin_bp.route("/admin/logout")
def admin_logout():

    session.clear()

    return redirect("/admin/login-page")