import os
import sys
import hashlib

from werkzeug.security import check_password_hash

from Manager_App import create_database, app
from Manager_App.models import Base, Entry, Group, Config, db

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
            
            master_key = request.form.get("master_key")
            hash_master_key = db.get_or_404(entity=Config.query, ident=Config.master_key)
            if check_password_hash(hash_master_key, master_key) is False:
                raise PermissionError
            
            return redirect(url_for("views.workspace", db_name=db_name))

        except FileNotFoundError:
            print("1q23412312s")
            flash("Master Password is False", category="error")
        except PermissionError:
            print("122421caf")
            flash("Database doesn't exist", category="error")
        #except Exception:
        #    print("sacaec")
        #    flash("Something happened I don't know of", category="critical_error")
    return render_template("index.html")


@auth.route("/createDatabase", methods=["POST","GET"])
def createDatabase():
    if request.method == "POST":
        try:
            db_name = request.form.get("db_name")
            if os.path.exists(f"data/Datenbank.db") is False:
                with app.app_context():
                    print("WPUica")
                    db.create_all()
            else:
                print("FUCK YOU")
                raise FileExistsError
            
            configuration = Config(
                master_key = hashlib.sha256(request.form.get("master_key").encode(), usedforsecurity=True).hexdigest(),
            )
            
            #db.session.add(configuration)
            #db.session.commit()
            
            return redirect(url_for("auth.openDatabase"))
    
        except FileExistsError:
            flash("Database Already Exists", category="error")
            
    return render_template("createDatabase.html")
