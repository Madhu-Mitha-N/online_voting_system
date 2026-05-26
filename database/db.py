import sqlite3

DATABASE_NAME = "database/voting.db"


def get_db_connection():
    conn = sqlite3.connect(
        DATABASE_NAME,
        timeout=10,
        check_same_thread=False
    )
    conn.row_factory = sqlite3.Row
    return conn