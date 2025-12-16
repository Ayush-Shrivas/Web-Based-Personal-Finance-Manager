from database import initialize_database
from auth import register_user, login_user
from transactions import add_transaction, list_transactions
from budgets import set_budget, check_budget
from reports import generate_report
from backup import backup_database, restore_database

def main():
    initialize_database()
    print("Personal Finance Manager")

    while True:
        print("\n1. Register\n2. Login\n3. Exit")
        choice = input("Choose: ")

        if choice == "1":
            u = input("Username: ")
            p = input("Password: ")
            print("Registered successfully" if register_user(u, p) else "Username already exists")

        elif choice == "2":
            u = input("Username: ")
            p = input("Password: ")
            user_id = login_user(u, p)
            if not user_id:
                print("Invalid credentials")
                continue

            while True:
                print("""
1. Add Income
2. Add Expense
3. View Transactions
4. Set Budget
5. Generate Report
6. Backup Data
7. Restore Data
8. Logout
""")
                c = input("Choose: ")

                if c == "1":
                    add_transaction(user_id, float(input("Amount: ")), input("Category: "), "income")
                elif c == "2":
                    category = input("Category: ")
                    amount = float(input("Amount: "))
                    add_transaction(user_id, amount, category, "expense")
                    budget = check_budget(user_id, category)
                    if budget and budget[0] > budget[1]:
                        print("WARNING: Budget exceeded")
                elif c == "3":
                    for t in list_transactions(user_id):
                        print(t)
                elif c == "4":
                    set_budget(user_id, input("Category: "), float(input("Limit: ")))
                elif c == "5":
                    i, e, s = generate_report(user_id)
                    print(f"Income: {i}, Expense: {e}, Savings: {s}")
                elif c == "6":
                    backup_database()
                    print("Backup completed")
                elif c == "7":
                    restore_database()
                    print("Restore completed")
                elif c == "8":
                    break

        else:
            break

if __name__ == "__main__":
    main()
