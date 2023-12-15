from flask import Blueprint, render_template, url_for, redirect, request
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user, current_user
from .models import User
from . import db

auth = Blueprint("auth", __name__)

@auth.route("/login/")
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.overview'))
    else:
        return render_template("login.html")

@auth.route("/login", methods=["POST"])
def login_post():
    # login code goes here
    email = request.form.get("email")
    password = request.form.get("password")
    remember = True if request.form.get("remember") else False

    user = User.query.filter_by(email=email).first()

    #check if the user actually exists
    #take the user-supplied password, hash it, and compare it to the hashed password in the database
    if not user or not check_password_hash(user.password, password):
        return render_template("login.html", wrongLogin=True)
    else:
        login_user(user, remember=remember)
        return redirect(url_for("main.overview")) #redirect to main overview if login is correct

@auth.route("/signup/")
def signup():
    if current_user.is_authenticated:
        return redirect(url_for('main.overview'))
    else:
        return render_template("signup.html")

@auth.route("/signup/", methods=["POST"])
def signup_post():
    if current_user.is_authenticated:
        return redirect(url_for('main.overview'))
    #get input data
    email = request.form.get("email")
    name = request.form.get('name')
    password = request.form.get('password')

    user = User.query.filter_by(email=email).first() #check if acc with email already exists

    if user:
        return render_template("signup.html", emailUsed=True, email=email, name=name) #User with email already existing
    else:
        #add new user in Database
        newUser = User(email=email, name=name, password=generate_password_hash(password, method='sha256'))
        db.session.add(newUser)
        db.session.commit()

        login_user(newUser, remember=False)
        return redirect(url_for("main.overview"))

@auth.route("/logout/")
@login_required
def logout():
    logout_user()
    return redirect(url_for("main.home"))