import secrets

from UI_SERVER import dbConfuese as DB
from flask import Blueprint, render_template, request


views = Blueprint("views", __name__)

Database = secrets.token_hex()

@views.route("/")
def home():
    return render_template("home.html", text=Database)

@views.route("/insert_entry", methods=["GET", "POST"])
def insert_entry():
    if request.method == "POST":
        UserName = request.form.get("UserName")
        Password = request.form.get("Password")
        Notes = request.form.get("Notes")
        Title = request.form.get("Title")
        
        db = DB.DB("DATABASE")
        db.insert_entry(Title, UserName, Password, Notes)
    return render_template("insert_entry.html")