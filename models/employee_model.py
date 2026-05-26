from database.db import get_db_connection


def create_employee_table():

    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("""

        CREATE TABLE IF NOT EXISTS employees (

            employee_id INTEGER PRIMARY KEY,

            name TEXT NOT NULL,

            email TEXT UNIQUE,

            password TEXT NOT NULL,

            is_default_password INTEGER DEFAULT 1
        )

    """)

    conn.commit()
    conn.close()

# CREATE
def create_employee(data):

    conn = get_db_connection()
    cursor = conn.cursor()

    default_password = f"Emp@{data['employee_id']}"

    cursor.execute("""
    INSERT INTO employees (
        employee_id,
        name,
        email,
        password,
        is_default_password
    )
    VALUES (?, ?, ?, ?, ?)
""", (
    data["employee_id"],
    data["name"],
    data["email"],
    default_password,
    1
))

    conn.commit()
    conn.close()

# LOGIN
def employee_login(email, password):
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT * FROM employees
        WHERE email = ? AND password = ?
    """, (email, password))

    row = cursor.fetchone()
    conn.close()
    return row


# GET ALL EMPLOYEES
def get_all_employees():
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM employees")
    rows = cursor.fetchall()

    conn.close()
    return rows

# DELETE EMPLOYEE
def delete_employee(employee_id):

    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("""
        DELETE FROM employees
        WHERE employee_id = ?
    """, (employee_id,))

    conn.commit()
    conn.close()


# GET SINGLE EMPLOYEE
def get_employee_by_id(employee_id):

    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT * FROM employees
        WHERE employee_id = ?
    """, (employee_id,))

    row = cursor.fetchone()

    conn.close()
    return row


# COUNT EMPLOYEES
def count_employees():

    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT COUNT(*) as total
        FROM employees
    """)

    result = cursor.fetchone()

    conn.close()

    return result["total"]

# DELETE EMPLOYEE
def delete_employee(employee_id):

    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("""
        DELETE FROM employees
        WHERE employee_id = ?
    """, (employee_id,))

    conn.commit()
    conn.close()

# VERIFY PASSWORD
def verify_employee_password(employee_id, password):

    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("""

        SELECT * FROM employees

        WHERE employee_id = ?
        AND password = ?

    """, (employee_id, password))

    employee = cursor.fetchone()

    conn.close()

    return employee


# CHANGE PASSWORD
def change_employee_password(employee_id, new_password):

    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("""

        UPDATE employees

        SET
            password = ?

        WHERE employee_id = ?

    """, (new_password, employee_id))

    conn.commit()
    conn.close()


# UPDATE PROFILE
def update_employee_profile(employee_id, data):

    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("""

        UPDATE employees

        SET
            name = ?,
            email = ?

        WHERE employee_id = ?

    """, (

        data["name"],
        data["email"],
        employee_id

    ))

    conn.commit()
    conn.close()

