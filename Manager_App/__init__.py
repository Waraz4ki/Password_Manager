import secrets
import os

from Manager_App.models import db
from flask import Flask

db_na = "Datenbank"


def create_app():
    global app
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "q2w3oiuzqgbuzfgbqwoi9fqgfvq34097nq3oi"
    app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite+pysqlite:///{db_na}.db"
    #app.config["SQLALCHEMY_ENGINE_OPTIONS"] = "echo=True"
    #app.config["DATABASE"] = os.path.join(app.instance_path,"")
    
    db.init_app(app)
    
    with app.app_context():
        db.create_all()
    
    from .views import views
    from .auth import auth
    
    app.register_blueprint(views)
    app.register_blueprint(auth)

    return app

def create_database(db_name):
    if not os.path.exists(f"/data/{db_name}.db"):
        db.create_all()
        print('Created Database!')