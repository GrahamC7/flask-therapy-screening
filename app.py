from flask import Flask, render_template, request, redirect, url_for
import sqlite3
from datetime import datetime

app = Flask(__name__)

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

@app.route("/")
def form():
    return render_template("form.html")

@app.route("/submit", methods=["POST"])
def submit():
    # get form data
    first_name = request.form["first_name"]
    last_name = request.form["last_name"]
    date_of_birth = request.form["date_of_birth"]
    therapist_name = request.form["therapist_name"]

    # store data in database
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
    init_db()
    app.run(debug=True)