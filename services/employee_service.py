
import re

from models.employee_model import (
    create_employee,
    employee_login,
    get_all_employees,
    delete_employee,
    verify_employee_password,
    change_employee_password,
    update_employee_profile
)

# =========================
# CREATE EMPLOYEE
# =========================
def create_employee_service(data):
    create_employee(data)


# =========================
# LOGIN EMPLOYEE
# =========================
def employee_login_service(email, password):
    return employee_login(email, password)


# =========================
# GET ALL EMPLOYEES
# =========================
def get_all_employees_service():
    return get_all_employees()


# =========================
# DELETE EMPLOYEE
# =========================
def delete_employee_service(employee_id):
    delete_employee(employee_id)


# =========================
# VERIFY PASSWORD
# =========================
def verify_employee_password_service(employee_id, password):
    return verify_employee_password(employee_id, password)


# =========================
# CHANGE PASSWORD
# =========================
def change_employee_password_service(employee_id, new_password):

    if not validate_password(new_password):
        return False


# =========================
# UPDATE PROFILE
# =========================
def update_employee_profile_service(employee_id, data):
    update_employee_profile(employee_id, data)


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