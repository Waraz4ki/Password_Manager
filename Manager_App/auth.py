import os
import sys
import hashlib

from werkzeug.security import check_password_hash

from Manager_App.better_models import Base, Entry, Group, Database, db

from sqlalchemy import insert, select
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
            
            #TODO Check if Database does or does not exist
            
            master_key = hashlib.sha256(request.form.get("master_key").encode(), usedforsecurity=True).hexdigest()
            print(master_key)
            
            #! 1 Error only exists when relationship stuff is in use
            hashed_master_key = db.session.execute(select(Database.master_key).where(Database.name==db_name)).fetchone()[0]
            print(hashed_master_key)
                      
            if master_key == hashed_master_key:
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
            master_key = hashlib.sha256(request.form.get("master_key").encode(), usedforsecurity=True).hexdigest()
            
            #TODO Check if database already exists
            
            db.session.execute(insert(Database).values(
                {"name":db_name, "master_key":master_key}
            ))
            db.session.commit()
            
            return redirect(url_for("auth.openDatabase"))
    
        except FileExistsError:
            flash("Database Already Exists", category="error")
            
    return render_template("createDatabase.html")
