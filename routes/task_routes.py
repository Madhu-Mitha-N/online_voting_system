from flask import Blueprint
from controllers.task_controller import assign_task_controller
from controllers.task_controller import update_task_controller
from controllers.task_controller import (
    get_all_tasks_controller,
    delete_task_controller
)

task_bp = Blueprint("task_bp", __name__)

@task_bp.route("/task/assign", methods=["POST"])
def assign_task():
    return assign_task_controller()

@task_bp.route("/task/update/<int:task_id>", methods=["PUT"])
def update_task(task_id):
    return update_task_controller(task_id)

@task_bp.route("/task/all", methods=["GET"])
def get_all_tasks():
    return get_all_tasks_controller()


@task_bp.route("/task/delete/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):
    return delete_task_controller(task_id)