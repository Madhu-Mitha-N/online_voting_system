from flask import Blueprint, render_template

frontend_bp = Blueprint("frontend_bp", __name__)


# =====================================================
# HOME
# =====================================================

@frontend_bp.route("/")
def home():
    return render_template("admin/admin_login.html")


# =====================================================
# ADMIN PAGES
# =====================================================

# ADMIN CREATE PAGE
@frontend_bp.route("/admin/create-page")
def admin_create_page():
    return render_template("admin/admin_create.html")


# ADMIN LOGIN PAGE
@frontend_bp.route("/admin/login-page")
def admin_login_page():
    return render_template("admin/admin_login.html")


# ADMIN DASHBOARD
@frontend_bp.route("/admin/dashboard")
def admin_dashboard_page():
    return render_template("admin/admin_dashboard.html")


# VOTER MANAGEMENT
@frontend_bp.route("/admin/voter-management")
def voter_management_page():
    return render_template("admin/voter_management.html")

@frontend_bp.route("/admin/add-voter")
def add_voter_page():
    return render_template(
        "admin/add_voter.html"
    )

# CANDIDATE MANAGEMENT
@frontend_bp.route("/admin/candidate-management")
def candidate_management_page():
    return render_template("admin/candidate_management.html")


@frontend_bp.route("/admin/add-candidate")
def add_candidate_page():
    return render_template("admin/add_candidate.html")


# EMPLOYEE MANAGEMENT
@frontend_bp.route("/admin/employee-management")
def employee_management_page():
    return render_template("admin/employee_management.html")


# ASSIGN TASK PAGE
@frontend_bp.route("/admin/assign-task")
def assign_task_page():
    return render_template("admin/assign_task.html")


# STATISTICS PAGE
@frontend_bp.route("/admin/statistics")
def statistics_page():
    return render_template("admin/statistics.html")


# =====================================================
# VOTER PAGES
# =====================================================

# VOTER LOGIN
@frontend_bp.route("/voter/login-page")
def voter_login_page():
    return render_template("voter/voter_login.html")


# VOTER DASHBOARD
@frontend_bp.route("/voter/dashboard")
def voter_dashboard_page():
    return render_template("voter/voter_dashboard.html")


# VOTING PAGE
@frontend_bp.route("/voter/voting-page")
def voting_page():
    return render_template("voter/voting_page.html")


# VOTER PROFILE
@frontend_bp.route("/voter/profile")
def voter_profile_page():
    return render_template("voter/voter_profile.html")


# CHANGE PASSWORD
@frontend_bp.route("/voter/change-password")
def change_password_page():
    return render_template("voter/change_password.html")


# =====================================================
# EMPLOYEE PAGES
# =====================================================

# EMPLOYEE LOGIN
@frontend_bp.route("/employee/login-page")
def employee_login_page():
    return render_template("employee/employee_login.html")


# EMPLOYEE DASHBOARD
@frontend_bp.route("/employee/dashboard")
def employee_dashboard_page():
    return render_template("employee/employee_dashboard.html")


# EMPLOYEE PROFILE
@frontend_bp.route("/employee/profile")
def employee_profile_page():
    return render_template("employee/employee_profile.html")

# @frontend_bp.route("/admin/employee-management")
# def employee_management_page():
#     return render_template(
#         "admin/employee_management.html"
#     )


@frontend_bp.route("/admin/add-employee")
def add_employee_page():
    return render_template(
        "admin/add_employee.html"
    )


# @frontend_bp.route("/admin/assign-task")
# def assign_task_page():
#     return render_template(
#         "admin/assign_task.html"
#     )