from models.voter_model import count_voters
from models.candidate_model import count_candidates, get_candidate_ranking
from models.vote_model import count_votes


def get_dashboard_stats():

    return {
        "total_voters": count_voters(),
        "total_candidates": count_candidates(),
        "total_votes": count_votes()
    }


def get_ranking_service():

    rows = get_candidate_ranking()

    result = []

    for r in rows:
        result.append({
            "candidate_id": r["candidate_id"],
            "candidate_name": r["candidate_name"],
            "party_name": r["party_name"],
            "total_votes": r["total_votes"]
        })

    return result