import secrets
import os

from flask import Flask


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
