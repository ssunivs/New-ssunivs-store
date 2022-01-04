from flask import Flask
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from . import models
import config

db = SQLAlchemy()
migrate = Migrate()

# Flask-Login
login_manager = LoginManager()
login_manager.session_protection = "basic"
login_manager.login_view = "account.login"

bcrypt = Bcrypt()


def create_app():
    app = Flask(__name__)
    app.config.from_object(config)

    # set up extensions
    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)
    bcrypt = Bcrypt(app)

    # blueprint
    from .views import main_views
    app.register_blueprint(main_views.bp)

    from .auth import bp as auth_bp
    app.register_blueprint(auth_bp)

    return app
