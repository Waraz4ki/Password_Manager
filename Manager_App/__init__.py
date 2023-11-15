import secrets
import os

from flask import Flask
from flask_login import LoginManager

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import select, insert


db = SQLAlchemy()

def create_app():
    global app
    app = Flask(__name__)
    login_manager = LoginManager()
    app.config.update(
        ENVIROMENT = "developement",
        SECRET_KEY = "q37r9noj4c8qwz3ppppduzy9q88p0q0943ruc23498ur499qmx,jduoiwehgq87grtq968i7xtq48mx0qß1eßx120e0yüä1290u8k0a89zq9mx7r2zmnq39sik8ru94xrz8n20349xcr1ljx41ßqs49rlkdx",
        SQLALCHEMY_DATABASE_URI = f"sqlite+pysqlite:///Database.db",
    )
    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view="auth.openDatabase"
    
    from .better_models import Database, Group, Entry 
    
    if os.path.exists("///Database.db") is False:
        print("Tables Created")
        with app.app_context():
            db.create_all()
    
    @login_manager.user_loader
    def load_user(db_name):
        #db_id = db.session.execute(select(Database.id).where(Database.name==db_name)).fetchone()[0]
        return db.session.get(Database,1)
    
    #@login_manager.request_loader
    #def request_loader(request):
    #    db_name = request.form.get("master_key")
    #    db_id = db.session.execute(select(Database.id).where(Database.name==db_name)).fetchone()[0]
    #    return db.session.get(Database,db_id)
    
    from .views import views
    from .auth import auth
    
    app.register_blueprint(views)
    app.register_blueprint(auth)
    
    return app
