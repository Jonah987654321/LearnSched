from flask import render_template, redirect, Blueprint
from flask_login import login_required, current_user
from . import db
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
    return render_template('calendar.html')

@main.route("/timer/")
@login_required
def timer():
    return "Timer"

@main.route("/settings/")
@login_required
def settings():
    return "Settings"