import secrets

from flask_login import login_required, login_remembered, current_user
from flask import Blueprint, render_template, request, flash, redirect, url_for
from sqlalchemy import select, update, delete, insert

from Manager_App import db
from Manager_App.better_models import Database, Group, Entry


views = Blueprint("views", __name__)


@views.route("/workspace/<db_name><db_id>", methods=["GET", "POST"])
@login_required
def workspace(db_name, db_id):
    if request.method == "GET":
        try:
            global groups
            groups = db.session.execute(select(Group.group_name).where(Group.assigned_database_id==db_id)).all()
            return render_template("workspace.html", db_name=db_name, groups=groups)
        
        except IndexError:
            pass
        
    return render_template("workspace.html", db_name=db_name)


#@views.route(f"/workspace/{current_user}/add_entry", methods=["GET", "POST"])
#@login_required
#def add_entry():
#    if request.method == "POST":
#        try:
#            title = request.form.get("title")
#            name = request.form.get("name")
#            password = request.form.get("password")
#            url = request.form.get("url")
#            
#            #TODO Make sth. like current_group and use it
#            db.session.add(Entry(title=title, name=name, password=password, url=url, assigned_group_id=1))
#            return redirect(url_for("views.workspace"))
#        
#        except ValueError:
#            flash("Sth wnet wrong.", category="error")
#    
#    return render_template("add_entry.html")

#! On reload of this page db_name and group disappear
@views.route(f"/workspace/<db_name>/<group>", methods=["GET", "POST"])
@login_required
def get_group_entries(db_name, group):
    if request.method == "POST":
        group_id = db.session.execute(select(Group.id).where(Group.group_name==group)).fetchone()[0]
        
        entries = db.session.execute(select(Entry.title, Entry.name, Entry.password, Entry.url).where(Entry.assigned_group_id==group_id)).fetchall()
        print(entries)
        
        return render_template("workspace.html", db_name=db_name, groups=groups,entries=entries)

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
