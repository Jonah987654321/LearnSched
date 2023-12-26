from flask_login import UserMixin
from . import db

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))

class TodoLists(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100))
    icon = db.Column(db.String(100))
    userID = db.Column(db.Integer)

class Todos(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    task = db.Column(db.String(1000))
    dueDate = db.Column(db.DateTime())
    reminder = db.Column(db.DateTime())
    done = db.Column(db.Integer)
    userID = db.Column(db.Integer)
    listID = db.Column(db.Integer)

class Calendars(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(256))
    userID = db.Column(db.Integer)

class CalendarEntry(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(256))
    startTime = db.Column(db.DateTime())
    endTime = db.Column(db.DateTime())
    allDayEvent = db.Column(db.Boolean)
    calendarID = db.Column(db.Integer)

