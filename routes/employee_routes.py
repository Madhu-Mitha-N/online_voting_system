from flask import Blueprint
from controllers.employee_controller import *
employee_profile_password_change_controller

employee_bp = Blueprint("employee_bp", __name__)


@employee_bp.route("/employee/create", methods=["POST"])
def create():
    return create_employee_controller()


@employee_bp.route("/employee/login", methods=["POST"])
def login():
    return employee_login_controller()


@employee_bp.route("/employee/tasks/<int:employee_id>", methods=["GET"])
def tasks(employee_id):
    return get_employee_tasks_controller(employee_id)


@employee_bp.route("/employee/task/update/<int:task_id>", methods=["PUT"])
def update(task_id):
    return update_task_status_controller(task_id)

 # GET ALL
# @employee_bp.route("/employee/all", methods=["GET"])
# def get_all():
#     return get_all_employees_controller()


# DELETE
@employee_bp.route("/employee/delete/<int:employee_id>", methods=["DELETE"])
def delete(employee_id):
    return delete_employee_controller(employee_id)

# GET ALL EMPLOYEES
@employee_bp.route("/employee/all", methods=["GET"])
def get_all():
    return get_all_employees_controller()

# CHANGE PASSWORD
@employee_bp.route(
    "/employee/change-password/<int:employee_id>",
    methods=["PUT"]
)
def change_password(employee_id):

    return change_employee_password_controller(
        employee_id
    )


# UPDATE PROFILE
@employee_bp.route(
    "/employee/profile/update/<int:employee_id>",
    methods=["PUT"]
)
def update_profile(employee_id):

    return update_employee_profile_controller(
        employee_id
    )

# PROFILE PASSWORD CHANGE
@employee_bp.route(
    "/employee/profile-change-password/<int:employee_id>",
    methods=["PUT"]
)
def employee_profile_password_change_route(employee_id):

    return employee_profile_password_change_controller(
        employee_id
    )

# FIRST LOGIN PASSWORD CHANGE
@employee_bp.route(
    "/employee/change-password/<int:employee_id>",
    methods=["PUT"]
)
def employee_change_password_route(employee_id):

    return employee_change_password_controller(
        employee_id
    )