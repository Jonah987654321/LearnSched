from flask_login import UserMixin
from . import db

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))

class TodoLists(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    icon = db.Column(db.String(100))
    userID = db.Column(db.Integer)

class Todos(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String(1000))
    dueDate = db.Column(db.String(11))
    reminder = db.Column(db.String(11))
    done = db.Column(db.Integer)
    userID = db.Column(db.Integer)
    listID = db.Column(db.Integer)

class Calendars(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(256))
    userID = db.Column(db.Integer)

