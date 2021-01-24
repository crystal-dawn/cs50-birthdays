import os

from cs50 import SQL
from flask import Flask, flash, jsonify, redirect, render_template, request, session
import secrets
# Configure application
app = Flask(__name__)

secret = secrets.token_urlsafe(32)

app.secret_key = secret

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///birthdays.db")

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":

        # TODO: Add the users entry into the database
        name = request.form.get("name")
        month = request.form.get("month")
        day = request.form.get("day")

        # Validate name entered
        valid_name = name_entered(name)
        # Validate birthday entered
        valid_birthday = birthday_entered(month, day)
        # Validate it's not a duplicate entry
        unique_record = preexisting_record(name, month, day)

        if valid_name and valid_birthday and unique_record:
            flash("Success!", 'success')
            db.execute("INSERT INTO birthdays (name, month, day) VALUES (:name, :month, :day)", name=name, month=month, day=day)

        return redirect("/")

    else:

        # TODO: Display the entries in the database on index.html
        birthdays = db.execute("SELECT * FROM birthdays")

        return render_template("index.html", birthdays=birthdays)


def name_entered(name):
    ''' Flash error is name is not text, includes empty '''
    if not name.isalpha():
        flash("Please enter text name", "error")
    else:
        return True

def birthday_entered(month, day):
    ''' Flash error if month and birthday are not valid '''
    # Using February 29 to account for leap year
    # If user enters 31 for April, error will trigger
    maxDaysInMonth = {
        '30': [
            '4',
            '6',
            '9',
            '11'
        ],
        '29': [
            '2'
        ]
    }

    # Month or day are blank
    if not month or not day:
        flash('Please enter month and day', 'error')
    else:
        # Check if month/day combination is a valid possibility
        try:
            maxDaysInMonth[day]

            flash('That month has less days', 'error')
        except:
            return True


def preexisting_record(name, month, day):
    ''' Check for duplicates, show warning and tip to enter last name'''
    duplicate = db.execute("SELECT * FROM birthdays WHERE name = :name AND month = :month AND day = :day",
                name=name,
                month=month,
                day=day
                )
    # Flash warning and tip on proper data entry
    if duplicate:
        flash("Birthday record already exists", 'warning')
        flash('If this is not a duplicate, enter a last name or initial to save record.', 'info')
    else:
        return True