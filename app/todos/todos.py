from flask import render_template, redirect, Blueprint, request
from flask_login import login_required, current_user
from .. import db
from ..models import TodoLists, Todos

todos = Blueprint("todos", __name__, template_folder='templates', static_folder='static')

@todos.route("/")
@login_required
def todos_main():

    return render_template('todos/listview.html')

@todos.route("/new-list", methods=["POST"])
@login_required
def todos_newList():
    name = request.form.get("name")
    icon = request.form.get("icon") if request.form.get("icon") != "" else '<i class="fa-solid fa-list-check"></i>'

    createdList = TodoLists(name=name, icon=icon, userID=current_user.id)
    db.session.add(createdList)
    db.session.commit()

    return redirect("/todos/")