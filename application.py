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

        name_entered(name)
        birthday_entered(month, day)
        # Check for duplicates, show warning and tip to enter last name
        # Flash success after inserted into db
        # else:
        #     flash("Success!")

        return redirect("/")

    else:

        # TODO: Display the entries in the database on index.html
        birthdays = db.execute("SELECT * FROM birthdays")

        return render_template("index.html", birthdays=birthdays)


def name_entered(name):
    ''' Flash error is name is not text, includes empty '''
    if not name.isalpha():
        flash("Please enter text name", "error")

def birthday_entered(month, day):
    app.logger.info(month)
    app.logger.info(day)
    ''' Flash error if month and birthday are not valid '''
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

    if not month or not day:
        flash('Please enter monday and day', 'error')
        app.logger.info(maxDaysInMonth[day])
    else:
        try:
            maxDaysInMonth[day]

            flash('That month has less days', 'error')
        except:
            return None
        # If looking up the day in maxDaysInMonth throws a value error, one of the fields is blank...?
        # try:

        # except:
        #     flash('Please enter month and day')