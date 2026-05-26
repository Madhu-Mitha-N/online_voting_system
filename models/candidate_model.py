from database.db import get_db_connection


def create_candidate_table():
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS candidates (
            candidate_id INTEGER PRIMARY KEY AUTOINCREMENT,
            candidate_name TEXT NOT NULL,
            party_name TEXT NOT NULL,
            symbol TEXT,
            district TEXT,
            ward TEXT,
            total_votes INTEGER DEFAULT 0
        )
    """)

    conn.commit()
    conn.close()


# CREATE
def create_candidate(data):
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO candidates (
            candidate_name, party_name, symbol, district, ward
        ) VALUES (?, ?, ?, ?, ?)
    """, (
        data["candidate_name"],
        data["party_name"],
        data["symbol"],
        data["district"],
        data["ward"]
    ))

    conn.commit()
    conn.close()


# GET ALL (FOR VOTER DASHBOARD)
def get_all_candidates():
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM candidates")
    rows = cursor.fetchall()

    conn.close()
    return rows


# GET ONE
def get_candidate_by_id(candidate_id):
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM candidates WHERE candidate_id = ?", (candidate_id,))
    row = cursor.fetchone()

    conn.close()
    return row


# UPDATE
def update_candidate(candidate_id, data):
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE candidates
        SET candidate_name=?, party_name=?, symbol=?, district=?, ward=?
        WHERE candidate_id=?
    """, (
        data["candidate_name"],
        data["party_name"],
        data["symbol"],
        data["district"],
        data["ward"],
        candidate_id
    ))

    conn.commit()
    conn.close()


# DELETE
def delete_candidate(candidate_id):
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM candidates WHERE candidate_id=?", (candidate_id,))

    conn.commit()
    conn.close()

def increment_vote(candidate_id):
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE candidates
        SET total_votes = total_votes + 1
        WHERE candidate_id = ?
    """, (candidate_id,))

    conn.commit()
    conn.close()

def count_candidates():
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) as total FROM candidates")
    result = cursor.fetchone()

    conn.close()
    return result["total"]


def get_candidate_ranking():
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT candidate_id, candidate_name, party_name, total_votes
        FROM candidates
        ORDER BY total_votes DESC
    """)

    rows = cursor.fetchall()
    conn.close()
    return rows