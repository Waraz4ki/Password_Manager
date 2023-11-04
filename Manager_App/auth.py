import os
import sys
import hashlib

from Manager_App import __create_engine__
from Manager_App.models import Base, Entry, Group, Config
from sqlalchemy import select, insert
from flask import Blueprint, render_template, request, flash, redirect, url_for

auth = Blueprint("auth", __name__)


@auth.route("/test")
def test2():
    return render_template("organizethis.html")


@auth.route("/", methods=["GET", "POST"])
def open_database():
    if request.method == "POST":
        try:
            #! Look at Bcrypt or Argon2
            db_name = request.form.get("db_name")
            if os.path.exists(f"data/{db_name}.db") is False:
                raise FileNotFoundError
            
            master_key = hashlib.sha256(request.form.get("master_key").encode(), usedforsecurity=True).hexdigest()
            
            with __create_engine__(db_name).begin() as connection:
                res = connection.execute(select(Config.master_key))
                if res.first()[0] != master_key:
                    raise PermissionError
            return redirect(url_for("views.workspace", db_name=db_name))
        
        except PermissionError:
            flash("Wrong Master Key", category="error")
        except FileNotFoundError:
            flash("Database doesn't exsit", category="error")
    
    return render_template("index.html")


@auth.route("/createDatabase", methods=["GET", "POST"])
def create_database():
    if request.method == "POST":
        try:
            db_name = request.form.get("db_name", default="Database")
            if os.path.exists(f"data/{db_name}.db") is False:
                Base.metadata.create_all(__create_engine__(db_name))
            else:
                raise FileExistsError
            
            master_key = hashlib.sha256(request.form.get("master_key").encode(), usedforsecurity=True).hexdigest()
    
            with __create_engine__(db_name).begin() as connection:
                connection.execute(insert(Config).values(master_key=master_key))
            return redirect(url_for("auth.open_database"))
            
        except FileExistsError:
            flash("Database Already Exists", category="error")

    return render_template("createDatabase.html")
