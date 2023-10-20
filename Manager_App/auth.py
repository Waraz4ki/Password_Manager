import os
import sys
import hashlib

from Manager_App.models import Base, Entry, Group
from flask import Blueprint, render_template, request, flash, redirect, url_for, get_flashed_messages
from sqlalchemy import create_engine, MetaData


auth = Blueprint("auth", __name__)

@auth.route("/test")
def test2():
    return render_template("organizethis.html")

def __create_engine__(__dbname__):
    engine = create_engine(f"sqlite:///data/{__dbname__}.db")
    return engine
    
@auth.route("/", methods=["GET", "POST"])
def open_database():
    if request.method == "POST":
        try:
            #! Look at Bcrypt or Argon2
            DB_NAME = request.form.get("DATABASE")
            masterKEY = hashlib.sha256(request.form.get("masterKEY").encode(), usedforsecurity=True).hexdigest()
        except FileNotFoundError:
            flash("Database doesn't exsit", category="error")
    return render_template("index.html")

@auth.route("/createDatabase", methods=["GET", "POST"])
def create_database():
    if request.method == "POST":
        DB_NAME = request.form.get("DATABASE")
        if os.path.exists(f"data/{DB_NAME}"):
            flash("Database already exists")
        else:
            masterKEY = hashlib.sha256(request.form.get("masterKEY").encode(), usedforsecurity=True).hexdigest()
            Base.metadata.create_all(__create_engine__(__dbname__=DB_NAME))
            return redirect(url_for("auth.open_database"))
    return render_template("createDatabase.html")


    

