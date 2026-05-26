from flask import request, jsonify
from services.vote_service import vote_service
from models.voter_model import get_voter_by_id
from models.vote_model import get_all_votes

def vote_controller():

    data = request.get_json()

    voter_id = data.get("voter_id")
    candidate_id = data.get("candidate_id")

    voter = get_voter_by_id(voter_id)

    if not voter:
        return jsonify({"error": "Voter not found"}), 404

    # CHECK IF ALREADY VOTED
    if voter["has_voted"] == 1:
        return jsonify({"error": "You have already voted"}), 400

    vote_service(voter_id, candidate_id)

    return jsonify({
        "message": "Vote submitted successfully"
    }), 200

def get_all_votes_controller():

    votes = get_all_votes()

    result = []

    for vote in votes:

        result.append({

            "vote_id": vote["vote_id"],

            "voter_id": vote["voter_id"],

            "candidate_id": vote["candidate_id"]

        })

    return jsonify(result), 200