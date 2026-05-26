from flask import request, jsonify
from services.task_service import assign_task_service
from models.task_model import update_task_status
from models.task_model import (
    get_all_tasks,
    delete_task
)

def update_task_controller(task_id):
    data = request.get_json()

    status = data.get("status")

    if not status:
        return jsonify({
            "error": "status required"
        }), 400

    update_task_status(task_id, status)

    return jsonify({
        "message": "Task updated successfully"
    }), 200
def assign_task_controller():
    data = request.get_json()

    task_name = data.get("task_name")
    employee_id = data.get("employee_id")

    if not task_name or not employee_id:
        return jsonify({
            "error": "task_name and employee_id required"
        }), 400

    assign_task_service(task_name, employee_id)

    return jsonify({
        "message": "Task assigned successfully"
    }), 201

def get_all_tasks_controller():

    tasks = get_all_tasks()

    result = []

    for t in tasks:

        result.append({

            "task_id": t["task_id"],
            "task_name": t["task_name"],
            "employee_name": t["employee_name"],
            "status": t["status"]

        })

    return jsonify(result), 200


def delete_task_controller(task_id):

    delete_task(task_id)

    return jsonify({
        "message": "Task deleted successfully"
    }), 200