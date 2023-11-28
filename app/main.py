from flask import render_template, redirect, Blueprint
from flask_login import login_required, current_user
from . import db
from app.helper import generate_full_weeks_array
main = Blueprint("main", __name__)

@main.route("/")
def home():
    return redirect("/overview")

@main.route("/overview/")
@login_required
def overview():
    return render_template('overview.html', name=current_user.name)

@main.route("/todos/")
@login_required
def todos():
    return render_template('todos.html')

@main.route("/calendar/")
@login_required
def calendar():
    return render_template('calendar.html', dates=generate_full_weeks_array(), entries={"2023-11-21": [{"title": "Test", "color": "red", "fullDay": False, "startTime": "11 AM", "duration": 60*60}], "2023-11-09": [{"title": "Test 2", "color": "blue", "fullDay": True, "startTime": "", "duration": 0}]})

@main.route("/timer/")
@login_required
def timer():
    return "Timer"

@main.route("/settings/")
@login_required
def settings():
    return "Settings"