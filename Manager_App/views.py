import secrets

from Manager_App.models import Base, Entry, Group, db
from flask import Blueprint, render_template, request, flash, redirect, url_for
from sqlalchemy import create_engine, MetaData, select, update, delete, insert

views = Blueprint("views", __name__)
db_name = "Datenbank"


@views.route("/workspace", methods=["GET", "POST"])
def workspace():
    if request.method == "GET":
        groups = db.session.execute(select(Group)).columns("group_name").all()
        #! Don't know why it doesn't work just gives me Keyerror...
        #TODO Fix it!
        entries = db.session.execute(select(Entry)).all()
        #entries = db.session.execute(select(Entry.title, Entry.name, Entry.password, Entry.url)).fetchall()
        print(entries)
        #entries = db.get_or_404(Entry, 1)
    
    return render_template("organizethis.html", db_name=db_name, groups=groups)


@views.route("/funcs/addEntry", methods = ["GET", "POST"])
def add_entry(): 
    if request.method == "POST":
        try:
            title = request.form.get("title")
            name = request.form.get("name")
            password = request.form.get("password", default=secrets.token_hex(32))
            url = request.form.get("url")
            
            db.session.execute(insert(Entry),[
                {"title":title, "name":name, "password":password, "url":url}
            ])        
            return redirect(url_for("views.workspace"))
            
        except ValueError:
            pass
    return render_template("addEntry.html")
