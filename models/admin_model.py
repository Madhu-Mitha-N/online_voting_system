from database.db import get_db_connection


def create_admin_table():
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS admins (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            admin_name TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL
        )
    """)

    conn.commit()
    conn.close()


# CREATE ADMIN
def create_admin(admin_name, password):
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO admins (admin_name, password)
        VALUES (?, ?)
    """, (admin_name, password))

    conn.commit()
    conn.close()


# GET ALL ADMINS
def get_all_admins():
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM admins")

    admins = cursor.fetchall()

    conn.close()

    return admins


# GET SINGLE ADMIN
def get_admin_by_id(admin_id):
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT * FROM admins
        WHERE id = ?
    """, (admin_id,))

    admin = cursor.fetchone()

    conn.close()

    return admin


# UPDATE ADMIN
def update_admin(admin_id, admin_name, password):
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE admins
        SET admin_name = ?, password = ?
        WHERE id = ?
    """, (admin_name, password, admin_id))

    conn.commit()
    conn.close()


# DELETE ADMIN
def delete_admin(admin_id):
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("""
        DELETE FROM admins
        WHERE id = ?
    """, (admin_id,))

    conn.commit()
    conn.close()


# ADMIN LOGIN
def admin_login(admin_name, password):
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT * FROM admins
        WHERE admin_name = ? AND password = ?
    """, (admin_name, password))

    admin = cursor.fetchone()

    conn.close()

    return admin