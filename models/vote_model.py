from database.db import get_db_connection


def create_vote_table():
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS votes (
            vote_id INTEGER PRIMARY KEY AUTOINCREMENT,
            voter_id INTEGER UNIQUE,
            candidate_id INTEGER,
            voted_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    conn.commit()
    conn.close()


def insert_vote(voter_id, candidate_id):
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO votes (voter_id, candidate_id)
        VALUES (?, ?)
    """, (voter_id, candidate_id))

    conn.commit()
    conn.close()

def count_votes():
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) as total FROM votes")
    result = cursor.fetchone()

    conn.close()
    return result["total"]

def get_all_votes():

    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT * FROM votes
    """)

    rows = cursor.fetchall()

    conn.close()

    return rows