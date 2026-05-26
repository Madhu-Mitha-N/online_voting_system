from flask import Flask

from routes.admin_routes import admin_bp

from models.admin_model import create_admin_table
from models.voter_model import create_voter_table
from models.candidate_model import create_candidate_table
from models.employee_model import create_employee_table
from models.task_model import create_task_table
from models.vote_model import create_vote_table
from routes.voter_routes import voter_bp
from routes.candidate_routes import candidate_bp
from routes.vote_routes import vote_bp
from routes.admin_dashboard_routes import dashboard_bp
from routes.employee_routes import employee_bp
from routes.task_routes import task_bp
from routes.frontend_routes import frontend_bp




app = Flask(__name__)

# REGISTER BLUEPRINT
app.register_blueprint(admin_bp)
app.register_blueprint(voter_bp)
app.register_blueprint(candidate_bp)
app.register_blueprint(vote_bp)
app.register_blueprint(dashboard_bp)
app.register_blueprint(employee_bp)
app.register_blueprint(task_bp)
app.register_blueprint(frontend_bp)
app.secret_key = "your_secret_key"

@app.route("/")
def home():
    return "Online Voting System Backend Running"


# CREATE TABLES
create_admin_table()
create_voter_table()
create_candidate_table()
create_employee_table()
create_task_table()
create_vote_table()


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5001,
        debug=True,
        use_reloader=False
    )