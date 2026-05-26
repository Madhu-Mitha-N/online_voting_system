from models.task_model import get_db_connection

def assign_task_service(task_name, employee_id):
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO tasks (task_name, employee_id, status)
        VALUES (?, ?, 'Pending')
    """, (task_name, employee_id))

    conn.commit()
    conn.close()