from models.vote_model import insert_vote
from models.voter_model import mark_voted
from models.candidate_model import increment_vote


def vote_service(voter_id, candidate_id):

    # INSERT INTO VOTES TABLE
    insert_vote(voter_id, candidate_id)

    # MARK VOTER AS VOTED
    mark_voted(voter_id)

    # INCREMENT CANDIDATE VOTE
    increment_vote(candidate_id)

# from models.voter_model import mark_voted
# from models.candidate_model import increment_vote
# from models.vote_model import insert_vote


# def vote_service(voter_id, candidate_id):

#     # 1. mark voter as voted
#     mark_voted(voter_id)

#     # 2. increase candidate vote
#     increment_vote(candidate_id)

#     # 3. store vote record
#     insert_vote(voter_id, candidate_id)

#     return True

