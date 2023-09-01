from flask import render_template, redirect, Blueprint
from . import db
main = Blueprint("main", __name__)

@main.route("/")
def home():
    return redirect("/overview")

@main.route("/overview/")
def overview():
    return render_template('overview.html')

@main.route("/todos/")
def todos():
    return render_template('todos.html')

@main.route("/calendar/")
def calendar():
    return render_template('calendar.html')

@main.route("/timer/")
def timer():
    return "Timer"

@main.route("/settings/")
def settings():
    return "Settings"