from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from app.helper import env

# init SQLAlchemy
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    app.config["SECRET_KEY"] = env("SQLITE_KEY")
    app.config["SQLALCHEMY_DATABASE_URI"] = env("SQLITE_URI")

    db.init_app(app)

    loginManager = LoginManager()
    loginManager.login_view = 'auth.login'
    loginManager.init_app(app)

    from . import models
    @loginManager.user_loader
    def load_user(userID):
        return models.User.query.get(int(userID))

    # blueprint for auth routes in our app
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    # blueprint for non-auth parts of app
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    with app.app_context():
        db.create_all()

    return app