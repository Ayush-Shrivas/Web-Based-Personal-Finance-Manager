from database import get_connection

def generate_report(user_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT type, SUM(amount)
        FROM transactions
        WHERE user_id=?
        GROUP BY type
    """, (user_id,))

    rows = cursor.fetchall()
    conn.close()

    income = sum(r[1] for r in rows if r[0] == "income")
    expense = sum(r[1] for r in rows if r[0] == "expense")
    return income, expense, income - expense
