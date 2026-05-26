from flask import request, jsonify

from services.candidate_service import (
    create_candidate_service,
    get_all_candidates_service,
    get_single_candidate_service,
    update_candidate_service,
    delete_candidate_service
)


# CREATE
def create_candidate_controller():
    data = request.get_json()

    create_candidate_service(data)

    return jsonify({
        "message": "Candidate created successfully"
    }), 201


# GET ALL (IMPORTANT FOR VOTING UI)
def get_all_candidates_controller():
    rows = get_all_candidates_service()

    result = []
    for c in rows:
        result.append({
            "candidate_id": c["candidate_id"],
            "candidate_name": c["candidate_name"],
            "party_name": c["party_name"],
            "symbol": c["symbol"],
            "district": c["district"],
            "ward": c["ward"],
            "total_votes": c["total_votes"]
        })

    return jsonify(result), 200


# GET ONE
def get_single_candidate_controller(candidate_id):
    c = get_single_candidate_service(candidate_id)

    if not c:
        return jsonify({"error": "Candidate not found"}), 404

    return jsonify(dict(c)), 200


# UPDATE
def update_candidate_controller(candidate_id):
    data = request.get_json()

    update_candidate_service(candidate_id, data)

    return jsonify({
        "message": "Candidate updated successfully"
    }), 200


# DELETE
def delete_candidate_controller(candidate_id):
    delete_candidate_service(candidate_id)

    return jsonify({
        "message": "Candidate deleted successfully"
    }), 200