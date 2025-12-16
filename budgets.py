from database import get_connection

def set_budget(user_id, category, limit_amount):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO budgets (user_id, category, limit_amount)
        VALUES (?, ?, ?)
    """, (user_id, category, limit_amount))
    conn.commit()
    conn.close()

def check_budget(user_id, category):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT limit_amount FROM budgets
        WHERE user_id=? AND category=?
    """, (user_id, category))
    budget = cursor.fetchone()

    if not budget:
        return None

    cursor.execute("""
        SELECT SUM(amount) FROM transactions
        WHERE user_id=? AND category=? AND type='expense'
    """, (user_id, category))
    spent = cursor.fetchone()[0] or 0

    conn.close()
    return spent, budget[0]
