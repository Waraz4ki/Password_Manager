import secrets
import os

from flask import Flask
from Manager_App.models import Group, Entry
from sqlalchemy import create_engine, select

def __create_engine__(__db_name__):
    engine = create_engine(f"sqlite:///data/{__db_name__}.db")
    return engine

def create_app():
    app = Flask(__name__)
    app.config.from_mapping(
        SECRET_KEY = "adfhbatg",
        DATABASE = os.path.join(app.instance_path,"")
    )
    
    from .views import views
    from .auth import auth
    
    app.register_blueprint(views)
    app.register_blueprint(auth)

    return app
