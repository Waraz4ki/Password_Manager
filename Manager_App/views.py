import secrets
import os

from Manager_App import __create_engine__
from Manager_App.models import Base, Entry, Group, Config
from flask import Blueprint, render_template, request, flash, redirect, url_for
from sqlalchemy import select, update, delete, insert

views = Blueprint("views", __name__)
#db_name = "Datenbank"


@views.route("/workspace/<db_name>", methods=["GET", "POST"])
def workspace(db_name):
    if request.method == "GET":
        
        with __create_engine__(db_name).begin() as connection:
            groups = connection.execute(select(Group)).columns("group_name").all()
            entries = connection.execute(select(Entry)).columns("title","name","password","url").all()
                
    return render_template("workspace.html", database=db_name, entries=entries, groups=groups)


@views.route("/funcs/addEntry", methods = ["GET", "POST"])
def add_entry(db_name):
    if request.method == "POST":
        try:
            title = request.form.get("title")
            name = request.form.get("name")
            password = request.form.get("password", default=secrets.token_hex(32))
            url = request.form.get("url")

            with __create_engine__(db_name).begin() as connection:
                connection.execute(insert(Entry),[
                    {"title":title, "name":name, "password":password, "url":url}
                ],)
            return redirect(url_for("views.workspace"))
        
        except ValueError:
            pass
    return render_template("addEntry.html")