import os
import sys
import hashlib

from flask_login import login_user, login_required, logout_user, current_user
from flask import Blueprint, render_template, flash, redirect, url_for, request, make_response, abort

from sqlalchemy import insert, select

from Manager_App import db
from Manager_App.better_models import Entry, Group, Database

auth = Blueprint("auth", __name__)


@auth.route("/", methods=["GET", "POST"])
def open_database():
    if request.method == "POST":
        try:
            db_name = request.form.get("db_name")
            db_id = db.session.execute(select(Database.id).where(Database.name==db_name)).fetchone()[0]
            #TODO Check if Database already exists!!!!

            master_key = hashlib.sha256(request.form.get("master_key").encode(), usedforsecurity=True).hexdigest()
            hashed_master_key = db.session.execute(select(Database.master_key).where(Database.id==db_id)).fetchone()[0]

            if hashed_master_key == master_key:
                db_obj = db.session.get(Database, db_id)
                login_user(db_obj)

                return redirect(url_for("views.workspace", db_name=db_name, db_id=db_id))
        except TypeError:
            flash("Database doesn't exist", category="error")
    return render_template("index.html")


@auth.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("auth.open_database"))


@auth.route("/create_database", methods=["POST","GET"])
def create_database():
    if request.method == "POST":
        try:
            db_name = request.form.get("db_name")
            master_key = hashlib.sha256(request.form.get("master_key").encode(), usedforsecurity=True).hexdigest()
            #TODO Check if database already exists
            
            db.session.add(Database(name=db_name, master_key=master_key))
            
            #id = db.session.execute(select(Database.id).where(Database.name==db_name)).fetchone()[0]
            #
            #db.session.add(Group(group_name=db_name, assigned_database_id=id))
            db.session.commit()
            
            return redirect(url_for("auth.open_database"))
    
        except FileExistsError:
            flash("Database Already Exists", category="error")
            
    return render_template("create_database.html")
