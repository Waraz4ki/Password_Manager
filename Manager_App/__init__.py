import secrets
import os

from flask_sqlalchemy import SQLAlchemy
from flask import Flask

db = SQLAlchemy()

def create_app():
    global app
    app = Flask(__name__)
    app.config.update(
        ENVIROMENT = "developement",
        SECRET_KEY = "q37r9noj4c8qwz3ppppduzy9q88p0q0943ruc23498ur499qmx,jduoiwehgq87grtq968i7xtq48mx0qß1eßx120e0yüä1290u8k0a89zq9mx7r2zmnq39sik8ru94xrz8n20349xcr1ljx41ßqs49rlkdx",
        SQLALCHEMY_DATABASE_URI = f"sqlite+pysqlite:///.db",
    )
    db.init_app(app)
    
    from .models import Config, Entry, Group
    
    from .views import views
    from .auth import auth
    
    app.register_blueprint(views)
    app.register_blueprint(auth)

    return app
