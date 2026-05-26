from database.db import get_db_connection


# CREATE TABLE
def create_voter_table():
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS voters (
            voter_id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            phone TEXT,
            dob TEXT,
            district TEXT,
            ward TEXT,
            email TEXT UNIQUE,
            password TEXT NOT NULL,
            is_default_password INTEGER DEFAULT 1,
            has_voted INTEGER DEFAULT 0,
            profile_pic TEXT
        )
    """)

    conn.commit()
    conn.close()


# CREATE VOTER
def create_voter(voter_data):
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO voters (
            voter_id,
            name,
            phone,
            dob,
            district,
            ward,
            email,
            password
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        voter_data["voter_id"],
        voter_data["name"],
        voter_data["phone"],
        voter_data["dob"],
        voter_data["district"],
        voter_data["ward"],
        voter_data["email"],
        voter_data["password"]
    ))

    conn.commit()
    conn.close()


# GET ALL VOTERS
def get_all_voters():
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM voters")

    voters = cursor.fetchall()

    conn.close()

    return voters


# GET SINGLE VOTER
def get_voter_by_id(voter_id):
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT * FROM voters
        WHERE voter_id = ?
    """, (voter_id,))

    voter = cursor.fetchone()

    conn.close()

    return voter


# UPDATE VOTER
def update_voter(voter_id, voter_data):
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE voters
        SET
            name = ?,
            phone = ?,
            dob = ?,
            district = ?,
            ward = ?,
            email = ?
        WHERE voter_id = ?
    """, (
        voter_data["name"],
        voter_data["phone"],
        voter_data["dob"],
        voter_data["district"],
        voter_data["ward"],
        voter_data["email"],
        voter_id
    ))

    conn.commit()
    conn.close()


# DELETE VOTER
def delete_voter(voter_id):
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("""
        DELETE FROM voters
        WHERE voter_id = ?
    """, (voter_id,))

    conn.commit()
    conn.close()


# LOGIN
def voter_login(voter_id, password):
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT * FROM voters
        WHERE voter_id = ? AND password = ?
    """, (voter_id, password))

    voter = cursor.fetchone()

    conn.close()

    return voter


# CHANGE PASSWORD
def change_voter_password(voter_id, new_password):
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE voters
        SET password = ?, is_default_password = 0
        WHERE voter_id = ?
    """, (new_password, voter_id))

    conn.commit()
    conn.close()

def mark_voted(voter_id):
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE voters
        SET has_voted = 1
        WHERE voter_id = ?
    """, (voter_id,))

    conn.commit()
    conn.close()

def count_voters():
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) as total FROM voters")
    result = cursor.fetchone()

    conn.close()
    return result["total"]

# VERIFY PASSWORD
def verify_voter_password(voter_id, password):

    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("""

        SELECT * FROM voters

        WHERE voter_id = ?
        AND password = ?

    """, (voter_id, password))

    voter = cursor.fetchone()

    conn.close()

    return voter


# UPDATE PROFILE
def update_voter_profile(voter_id, data):

    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("""

        UPDATE voters

        SET
            name = ?,
            phone = ?,
            district = ?,
            ward = ?,
            email = ?

        WHERE voter_id = ?

    """, (

        data["name"],
        data["phone"],
        data["district"],
        data["ward"],
        data["email"],
        voter_id

    ))

    conn.commit()
    conn.close()

