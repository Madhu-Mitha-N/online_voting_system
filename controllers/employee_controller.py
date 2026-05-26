from flask import request, jsonify
from database.db import get_db_connection
from models.employee_model import employee_login
from models.task_model import get_tasks_by_employee, update_task_status
from models.employee_model import create_employee
from models.employee_model import (
    create_employee,
    employee_login,
    get_all_employees,
    delete_employee,
    verify_employee_password,
    change_employee_password,
    update_employee_profile,
    verify_employee_password
)

# CREATE
# CREATE
def create_employee_controller():

    data = request.get_json()

    employee_id = data.get("employee_id")

    default_password = f"Emp@{employee_id}"

    employee_data = {

        "employee_id": employee_id,

        "name": data.get("name"),

        "email": data.get("email"),

        "password": default_password
    }

    create_employee(employee_data)

    return jsonify({

        "message": "Employee created successfully",

        "default_password": default_password

    }), 201

# LOGIN
def employee_login_controller():
    data = request.get_json()

    email = data.get("email")
    password = data.get("password")

    emp = employee_login(email, password)

    if not emp:
        return jsonify({"error": "Invalid credentials"}), 401

    return jsonify({
    "message": "Login success",
    "employee": {
        "employee_id": emp["employee_id"],
        "name": emp["name"],
        "is_default_password": emp["is_default_password"] if "is_default_password" in emp.keys() else 1
    }
}), 200
# GET TASKS
def get_employee_tasks_controller(employee_id):

    tasks = get_tasks_by_employee(employee_id)

    result = []

    for t in tasks:
        result.append({
            "task_id": t["task_id"],
            "task_name": t["task_name"],
            "status": t["status"]
        })

    return jsonify(result), 200


# UPDATE TASK STATUS
def update_task_status_controller(task_id):
    data = request.get_json()

    update_task_status(task_id, data["status"])

    return jsonify({
        "message": "Task updated"
    }), 200

# GET ALL EMPLOYEES
def get_all_employees_controller():

    rows = get_all_employees()

    result = []

    for e in rows:

        result.append({
            "employee_id": e["employee_id"],
            "name": e["name"],
            "email": e["email"]
        })

    return jsonify(result), 200


# DELETE EMPLOYEE
def delete_employee_controller(employee_id):

    delete_employee(employee_id)

    return jsonify({
        "message": "Employee deleted successfully"
    }), 200

# CHANGE PASSWORD
def change_employee_password_controller(employee_id):

    data = request.get_json()

    current_password = data.get("current_password")

    new_password = data.get("new_password")

    employee = verify_employee_password(
        employee_id,
        current_password
    )

    if not employee:

        return jsonify({
            "error":
            "Current password incorrect"
        }), 400

    change_employee_password(
        employee_id,
        new_password
    )

    return jsonify({
        "message":
        "Password changed successfully"
    }), 200

# UPDATE PROFILE
def update_employee_profile_controller(employee_id):

    data = request.get_json()

    update_employee_profile(
        employee_id,
        data
    )

    return jsonify({
        "message":
        "Profile updated successfully"
    }), 200

# PROFILE PASSWORD CHANGE
def employee_profile_password_change_controller(employee_id):

    data = request.get_json()

    current_password = data.get("current_password")
    new_password = data.get("new_password")

    employee = verify_employee_password(
        employee_id,
        current_password
    )

    if not employee:
        return jsonify({
            "error": "Current password incorrect"
        }), 400

    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE employees
        SET password = ?
        WHERE employee_id = ?
    """, (new_password, employee_id))

    conn.commit()
    conn.close()

    return jsonify({
        "message": "Password updated successfully"
    }), 200

# FIRST LOGIN PASSWORD CHANGE
def employee_change_password_controller(employee_id):

    data = request.get_json()

    new_password = data.get("new_password")

    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE employees
        SET
            password = ?,
            is_default_password = 0
        WHERE employee_id = ?
    """, (new_password, employee_id))

    conn.commit()
    conn.close()

    return jsonify({
        "message": "Password updated successfully"
    }), 200