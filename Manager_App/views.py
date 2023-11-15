import secrets

from flask_login import login_manager, login_required
from flask import Blueprint, render_template, request, flash, redirect, url_for
from sqlalchemy import select, update, delete, insert

from Manager_App import db
from Manager_App.better_models import Database, Group, Entry

views = Blueprint("views", __name__)


@views.route("/workspace/?db_name=<db_name>&db_id=<db_id>", methods=["GET", "POST"])
@login_required
def workspace(db_name, db_id):
    if request.method == "GET":
        try:
            groups = db.session.execute(select(Group.group_name).where(Group.assigned_database_id==db_id)).fetchall()[0]
            entries = db.session.execute(select(Entry.title, Entry.name, Entry.password, Entry.url)).fetchall()
            
            return render_template("workspace.html", db_name=db_name, groups=groups, entries=entries)
        except IndexError:
            pass
        #! Don't know why it doesn't work just gives me Keyerror...
        #TODO Fix it!
    return render_template("workspace.html", db_name=db_name)

#@views.route("/workspace/<db_name>/add_entry", methods = ["GET", "POST"])
#def add_entry(): 
#    if request.method == "POST":
#        try:
#            title = request.form.get("title")
#            name = request.form.get("name")
#            password = request.form.get("password", default=secrets.token_hex(32))
#            url = request.form.get("url")
#            
#            db.session.execute(insert(Entry).values({
#                "title":title, "name":name, "password":password, "url":url, "assigned_group_id": 1
#            }))
#            
#            #db.session.execute(insert(Entry),[
#            #    {"title":title, "name":name, "password":password, "url":url}
#            #])        
#            return redirect(url_for("views.workspace"))
#            
#        except ValueError:
#            pass
#    return render_template("addEntry.html")
