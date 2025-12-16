from database import get_connection
from datetime import datetime

def add_transaction(user_id, amount, category, t_type):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO transactions (user_id, amount, category, type, date)
        VALUES (?, ?, ?, ?, ?)
    """, (user_id, amount, category, t_type, datetime.now().strftime("%Y-%m-%d")))
    conn.commit()
    conn.close()

def list_transactions(user_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "SELECT id, amount, category, type, date FROM transactions WHERE user_id=?",
        (user_id,)
    )
    rows = cursor.fetchall()
    conn.close()
    return rows
