import sqlite3
import os
import sys
import hashlib

from UI_SERVER import db as DB
from flask import Blueprint, render_template, request, flash, redirect, url_for


auth = Blueprint("auth", __name__)


@auth.route("/view")
def test():
    return render_template("file_view.html")
    
    
@auth.route("/", methods=["GET", "POST"])
def open_database():
    if request.method == "POST":
        DATABASE = request.form.get("DATABASE")
        #try: 
        #   
        #    masterKEY = hashlib.sha256(request.form.get("masterKEY").encode(), usedforsecurity=True).hexdigest()
        #    print(masterKEY)
        #    db = DB.DBClass(DATABASE)
        #    db.openingCheck(masterKEY)
        #
        #except os.path.exists(DATABASE) is not True:
        #    flash("Database doesn't exsit")

        if os.path.exists(DATABASE) is not True:
            flash("Database doesn't exist")
        else:
            masterKEY = hashlib.sha256(request.form.get("masterKEY").encode(), usedforsecurity=True).hexdigest()
            print(masterKEY)
            db = DB.DBClass(DATABASE)
            db.openingCheck(masterKEY)
            
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
            db = DB.DBClass(DATABASE)
            db.firstSetup(masterKEY)
            return redirect(url_for("auth.open_database"))
    return render_template("createDatabase.html")
