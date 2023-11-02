import secrets

from Manager_App.models import Base, Entry, Group, db
from flask import Blueprint, render_template, request, flash, redirect, url_for
#from sqlalchemy import create_engine, MetaData, select, update, delete, insert

views = Blueprint("views", __name__)
db_name = "Datenbank"

#def __create_engine__(__db_name__):
#    engine = create_engine(f"sqlite:///data/{__db_name__}.db")
#    return engine


@views.route("/file", methods=["GET", "POST"])
def workspace(db_name):
    if request.method == "GET":
        groups = db.get_or_404(Group.group_name)
        entries = db.get_or_404(Entry.title, Entry.name, Entry.password, Entry.url)
    
    return render_template("organizethis.html", db_name=db_name, groups=groups, entries=entries)
        

#@views.route("/file", methods=["GET", "POST"])
#def file_view():
#    if request.method == "GET":
#        
#        with __create_engine__(db_name).begin() as connection:
#            entries = connection.execute(select(Entry)).columns("title","name","password","url").all()
#            print(entries)
#                
#    return render_template("organizethis.html", database=db_name, entries=entries)



@views.route("/funcs/addEntry", methods = ["GET", "POST"])
def add_entry():
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
            return redirect(url_for("views.file_view"))
        
        except ValueError:
            pass
    return render_template("addEntry.html")
