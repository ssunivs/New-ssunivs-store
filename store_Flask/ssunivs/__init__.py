from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
import store_Flask.config as config

db=SQLAlchemy()
migrate=Migrate()
def create_app():
    app=Flask(__name__)
    app.config.from_object(config)
    #ORM_mysql
    db.init_app(app)
    migrate.init_app(app,db)
    #blueprint
    from .views import main_views
    app.register_blueprint(main_views.bp)
    
    return app