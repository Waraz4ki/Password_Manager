# import secrets
# import string

from Manager_App import db as DB
from flask import Blueprint, render_template, request, flash


views = Blueprint("views", __name__)
DATABASE = "Datenbank"


@views.route("/home")
def home():
    return render_template("home.html")

@views.route("/file", methods=["GET", "POST"])
def file_view():
    if request.method == "GET":
        pass
    return render_template("organizethis.html", database = DATABASE)

@views.route("/insert_entry", methods=["GET", "POST"])
def insert_entry():
    if request.method == "POST":
        UserName = request.form.get("UserName")
        Password = request.form.get("Password")
        Notes = request.form.get("Notes")
        Title = request.form.get("Title")
        
        db = DB.DBClass("DATABASE")
        db.insert_entry(Title, UserName, Password, Notes)
    return render_template("insert_entry.html")

@views.route("/view_file", methods=["GET", "POST"])
def view_file():
    if request.method == "POST":
        db = DB.DBClass("DATABASE")
        data = db.get_every_entry()
    return render_template("view_file.html")
        