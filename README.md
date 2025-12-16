# FinTrack – Web-Based Personal Finance Manager

[![Python](https://img.shields.io/badge/Python-3.9%2B-blue.svg?logo=python)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-Web_Framework-black.svg?logo=flask)](https://flask.palletsprojects.com/)
[![SQLite](https://img.shields.io/badge/SQLite-Database-003B57.svg?logo=sqlite)](https://www.sqlite.org/)
[![HTML5](https://img.shields.io/badge/HTML5-Frontend-E34F26.svg?logo=html5)](https://developer.mozilla.org/en-US/docs/Web/HTML)
[![CSS3](https://img.shields.io/badge/CSS3-Styling-1572B6.svg?logo=css3)](https://developer.mozilla.org/en-US/docs/Web/CSS)

FinTrack is a modern, secure, and user-friendly **web-based personal finance management application** designed to help individuals effectively manage their income, expenses, budgets, and savings.

The application is built using **Python and Flask** on the backend with **SQLite** for persistent storage, and a clean, responsive frontend using **HTML5 and modern CSS**. It demonstrates strong backend logic, structured architecture, and real-world financial tracking capabilities.

---

## ✨ Key Features

- **Secure User Authentication**: User registration and login with hashed password storage.
- **Income & Expense Tracking**: Add, categorize, and manage financial transactions.
- **Financial Dashboard**: View real-time summaries of income, expenses, and savings.
- **Persistent Storage**: Reliable data storage using SQLite database.
- **Clean & Modern UI**: Responsive and visually appealing interface with modern CSS styling.
- **Modular Architecture**: Well-structured backend code for scalability and maintainability.
- **Session Management**: Secure user sessions handled by Flask.

---

## 🛠️ Tech Stack & Architecture

| Category | Technology |
|--------|------------|
| **Backend** | `Python`, `Flask` |
| **Database** | `SQLite 3` |
| **Frontend** | `HTML5`, `CSS3` |
| **Authentication** | Session-based (Flask) |
| **Version Control** | `Git`, `GitHub` |

---

## 📂 Project Structure

```
personal_finance_manager/
│
├── app.py # Flask application entry point
├── auth.py # Authentication logic
├── database.py # Database connection & initialization
├── transactions.py # Income & expense handling
├── budgets.py # Budget management
├── reports.py # Financial reports
├── backup.py # Backup & restore utilities
│
├── static/
│ └── style.css # Modern UI styling
│
└── templates/
├── login.html # Login page
├── register.html # Registration page
└── dashboard.html # Dashboard interface
```

---

## ⚙️ Installation & Local Setup

### 1. Clone the Repository
```bash
git clone https://github.com/Ayush-Shrivas/Web-Based-Personal-Finance-Manager.git
cd Web-Based-Personal-Finance-Manager
```

### 2. Install Dependencies
```sh
pip install flask
```

### 3.Run the Application
```sh
python app.py
```

### 4. Access the Application
Open your browser and navigate to:
http://127.0.0.1:5000

### 🔐 Security Considerations
-Passwords are hashed before storage
-Secure session-based authentication
-Controlled database interactions

### 📈 Future Enhancements
-Monthly and yearly financial analytics with charts
-Budget alerts and notifications
-Export reports to CSV or PDF
-Dark/Light mode toggle
-Cloud deployment (Render, Railway, etc.)

## 👤 Author

**Ayush Shrivas**

-   **GitHub**: [@Ayush-Shrivas](https://github.com/Ayush-Shrivas)
-   **LinkedIn**: [Ayush Shrivas](https://www.linkedin.com/in/ayush-shrivas-190475299/)
