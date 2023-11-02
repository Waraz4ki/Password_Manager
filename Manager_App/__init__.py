import secrets
import os

from flask_sqlalchemy import SQLAlchemy
from flask import Flask

db_name = "awda"
db = SQLAlchemy()

def create_app():
    global app
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "q2w3oiuzqgbuzfgbqwoi9fqgfvq34097nq3oi"
    #TODO Please figure out how I can define this later of update it cause app.config.update(...) doesn't work(it's for the database name)
    app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite+pysqlite:///{db_name}.db"
    #app.config["SQLALCHEMY_ENGINE_OPTIONS"] = "echo=True"
    db.init_app(app)
    
    from .models import Config, Entry, Group
    
    from .views import views
    from .auth import auth
    
    app.register_blueprint(views)
    app.register_blueprint(auth)

    return app
