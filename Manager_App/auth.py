import os
import sys
import hashlib

from werkzeug.security import check_password_hash

from Manager_App import app
from Manager_App.models import Base, Entry, Group, Config, db

from sqlalchemy import select
from flask import Blueprint, render_template, request, flash, redirect, url_for

auth = Blueprint("auth", __name__)

@auth.route("/test")
def test2():
    return render_template("organizethis.html")


@auth.route("/", methods=["GET", "POST"])
def openDatabase():
    if request.method == "POST":
        try:
            db_name = request.form.get("db_name")
            if os.path.exists(f"instance/{db_name}.db") is False:
                raise FileNotFoundError
            
            master_key = hashlib.sha256(request.form.get("master_key").encode(), usedforsecurity=True).hexdigest()
            print(master_key)
            hashed_master_key = db.session.execute(select(Config.master_key)).fetchone()[0]
            print(hashed_master_key)
            
            if master_key == hashed_master_key:
            #TODO If you have time figure out why this won't work
            #if check_password_hash(hashed_master_key, master_key):
                print("Success")
                return redirect(url_for("views.workspace", db_name=db_name))
            else:
                flash("Master Password is incorrect", category="error")
           
        except FileNotFoundError:
            print("Don't exist")
            flash("Database doesn't exist", category="error")
            
    return render_template("index.html")


@auth.route("/createDatabase", methods=["POST","GET"])
def createDatabase():
    if request.method == "POST":
        try:
            db_name = request.form.get("db_name")
            if os.path.exists(f"data/{db_name}.db"):
                app.config.update(
                    SQLALCHEMY_DATABASE_URI = f"sqlite:///{db_name}.db"
                )
                with app.app_context():
                    db.create_all()
            else:
                raise FileExistsError
            
            configuration = Config(
                master_key = hashlib.sha256(request.form.get("master_key").encode(), usedforsecurity=True).hexdigest(),
            )
            
            db.session.add(configuration)
            db.session.commit()
            
            return redirect(url_for("auth.openDatabase"))
    
        except FileExistsError:
            flash("Database Already Exists", category="error")
            
    return render_template("createDatabase.html")
