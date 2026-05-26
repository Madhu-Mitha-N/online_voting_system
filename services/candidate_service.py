from models.candidate_model import (
    create_candidate,
    get_all_candidates,
    get_candidate_by_id,
    update_candidate,
    delete_candidate
)


def create_candidate_service(data):
    create_candidate(data)


def get_all_candidates_service():
    return get_all_candidates()


def get_single_candidate_service(candidate_id):
    return get_candidate_by_id(candidate_id)


def update_candidate_service(candidate_id, data):
    update_candidate(candidate_id, data)


def delete_candidate_service(candidate_id):
    delete_candidate(candidate_id)