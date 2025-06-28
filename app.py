from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3
from datetime import datetime

app = Flask(__name__)
app.secret_key = "your_secret_key_here"  # required for flash messages

# database setup
def init_db():
    conn = sqlite3.connect("patients.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS patients (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL,
            date_of_birth TEXT NOT NULL,
            therapist_name TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    conn.commit()
    conn.close()

# initialize the database
init_db()

@app.route("/", methods=["GET"])
def form():
    return render_template("form.html")

@app.route("/submit", methods=["POST"])
def submit():
    # get form data with validation
    first_name = request.form.get('first_name', '').strip()
    last_name = request.form.get('last_name', '').strip()
    date_of_birth = request.form.get('date_of_birth', '').strip()
    therapist_name = request.form.get('therapist_name', '').strip()

    # validation
    errors = []
    # check for empty fields
    if not first_name:
        errors.append("First name is required")
    if not last_name:
        errors.append("Last name is required")
    if not date_of_birth:
        errors.append("Date of birth is required")
    if not therapist_name:
        errors.append("Therapist name is required")

    # validate date is in the past
    if date_of_birth:
        try:
            birth_date = datetime.strptime(date_of_birth, '%Y-%m-%d')
            if birth_date.date() >= datetime.now().date():
                errors.append("Date of birth must be in the past")
        except ValueError:
            errors.append("Invalid date format")

    # if validation fails, flash errors and redirect to form
    if errors:
        for error in errors:
            flash(error, 'error')
        return redirect(url_for('form'))

    # store data in database (only if validation passes)
    conn = sqlite3.connect("patients.db")
    cursor = conn.cursor()
    cursor.execute("""
                   INSERT INTO patients (first_name, last_name, date_of_birth, therapist_name)
                   VALUES (?, ?, ?, ?)
    """, (first_name, last_name, date_of_birth, therapist_name))
    conn.commit()
    conn.close()

    # pass data to confirmation template using Jinja2
    return render_template("confirmation.html",
                           first_name=first_name,
                           last_name=last_name,
                           date_of_birth=date_of_birth,
                           therapist_name=therapist_name)

if __name__ == "__main__":
    app.run(debug=True)