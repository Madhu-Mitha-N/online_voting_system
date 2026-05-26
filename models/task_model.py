from database.db import get_db_connection


def create_task_table():
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            task_id INTEGER PRIMARY KEY AUTOINCREMENT,
            task_name TEXT NOT NULL,
            employee_id INTEGER,
            status TEXT DEFAULT 'Pending'
        )
    """)

    conn.commit()
    conn.close()


def get_tasks_by_employee(employee_id):
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT * FROM tasks WHERE employee_id = ?
    """, (employee_id,))

    rows = cursor.fetchall()
    conn.close()
    return rows


def update_task_status(task_id, status):
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE tasks
        SET status = ?
        WHERE task_id = ?
    """, (status, task_id))

    conn.commit()
    conn.close()

def get_all_tasks():

    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("""

        SELECT
            tasks.task_id,
            tasks.task_name,
            tasks.status,
            employees.name as employee_name

        FROM tasks

        LEFT JOIN employees
        ON tasks.employee_id = employees.employee_id

    """)

    rows = cursor.fetchall()

    conn.close()

    return rows


def delete_task(task_id):

    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("""
        DELETE FROM tasks
        WHERE task_id = ?
    """, (task_id,))

    conn.commit()
    conn.close()