from flask import Flask, render_template, request, redirect, session, url_for
from auth import register_user, login_user
from transactions import add_transaction, list_transactions
from reports import generate_report
from database import initialize_database

app = Flask(__name__)
app.secret_key = "personal-finance-secret-key"

# Initialize database on startup
initialize_database()


@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        user_id = login_user(username, password)
        if user_id:
            session["user_id"] = user_id
            return redirect(url_for("dashboard"))
        else:
            return render_template("login.html", error="Invalid credentials")

    return render_template("login.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        if register_user(username, password):
            return redirect(url_for("login"))
        else:
            return render_template("register.html", error="Username already exists")

    return render_template("register.html")


@app.route("/dashboard")
def dashboard():
    if "user_id" not in session:
        return redirect(url_for("login"))

    user_id = session["user_id"]
    income, expense, savings = generate_report(user_id)
    transactions = list_transactions(user_id)

    return render_template(
        "dashboard.html",
        income=income,
        expense=expense,
        savings=savings,
        transactions=transactions
    )


@app.route("/add_transaction", methods=["POST"])
def add_transaction_route():
    if "user_id" not in session:
        return redirect(url_for("login"))

    amount = float(request.form["amount"])
    category = request.form["category"]
    t_type = request.form["type"]

    add_transaction(session["user_id"], amount, category, t_type)
    return redirect(url_for("dashboard"))


@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(debug=True)
