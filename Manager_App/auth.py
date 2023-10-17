import os
import sys
import hashlib

from Manager_App.models import Base, Entries, Groups
from flask import Blueprint, render_template, request, flash, redirect, url_for, get_flashed_messages
from sqlalchemy import create_engine, MetaData


auth = Blueprint("auth", __name__)
DB_NAME = "moritz"
engine = create_engine(f"sqlite:///data/{DB_NAME}.db")

@auth.route("/view")
def test():
    return render_template("file_view.html")

@auth.route("/test")
def test2():
    return render_template("organizethis.html")
    
@auth.route("/", methods=["GET", "POST"])
def open_database():
    if request.method == "POST":
        try:
            #! Look at Bcrypt or Argon2
            DATABASE = request.form.get("DATABASE")
            masterKEY = hashlib.sha256(request.form.get("masterKEY").encode(), usedforsecurity=True).hexdigest()
#            db = DB.DBClass(DATABASE)
#            if db.openingCheck() == masterKEY:
#                return redirect(url_for("views.file_view"))
#            else:
#                flash("Master Key is Wrong Please check your spelling", category="error")

        except FileNotFoundError:
            flash("Database doesn't exsit", category="error")
    return render_template("index.html")

@auth.route("/createDatabase", methods=["GET", "POST"])
def create_database():
    if request.method == "POST":
        DATABASE = request.form.get("DATABASE")
        if os.path.exists(DATABASE) is True:
            flash("Database already exists")
        else:
            masterKEY = hashlib.sha256(request.form.get("masterKEY").encode(), usedforsecurity=True).hexdigest()
            print(masterKEY)
            Base.metadata.create_all(engine)
    return render_template("createDatabase.html")
