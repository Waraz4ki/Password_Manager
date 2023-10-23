import os
import sys
import hashlib

from Manager_App.models import Base, Entry, Group, Config
from flask import Blueprint, render_template, request, flash, redirect, url_for, get_flashed_messages
from sqlalchemy import create_engine, MetaData, select, update, delete, insert


auth = Blueprint("auth", __name__)

@auth.route("/test")
def test2():
    return render_template("organizethis.html")

def __create_engine__(__db_name__):
    engine = create_engine(f"sqlite:///data/{__db_name__}.db")
    return engine

@auth.route("/", methods=["GET", "POST"])
def open_database():
    if request.method == "POST":

        try:
            #! Look at Bcrypt or Argon2
            db_name = request.form.get("DATABASE")
            master_key = hashlib.sha256(request.form.get("masterKEY").encode(), usedforsecurity=True).hexdigest()
            
            with __create_engine__(db_name).begin() as connection:
                res = connection.execute(select(Config.master_key))
                if res.first()[0] == master_key:
                    return redirect(url_for("views.file_view"))
                
        except os.path.exists(f"data/{db_name}.db"):
            flash("Database doesn't exsit", category="error")
    
    return render_template("index.html")

@auth.route("/createDatabase", methods=["GET", "POST"])
def create_database():
    if request.method == "POST":

        db_name = request.form.get("DATABASE", default="Database")
        if os.path.exists(f"data/{db_name}"):
            flash("Database already exists")
        else:
            master_key = hashlib.sha256(request.form.get("masterKEY").encode(), usedforsecurity=True).hexdigest()
            Base.metadata.create_all(__create_engine__(db_name))
            with __create_engine__(db_name).begin() as connection:
                connection.execute(insert(Config).values(master_key=master_key))
            return redirect(url_for("auth.open_database"))

    return render_template("createDatabase.html")


    

