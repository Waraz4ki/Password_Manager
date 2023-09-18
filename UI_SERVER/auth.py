from UI_SERVER import dbConfuese as DB
from AES import AESCipher
from flask import Blueprint, render_template, request, flash


auth = Blueprint("auth", __name__)
AES = AESCipher()


@auth.route("/Home", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        pass
    return render_template("home.html")

@auth.route("/open_database", methods=["GET", "POST"])
def open_database():
    if request.method == "POST":
        DATABASE = request.form.get("databaseText")
        db = DB.DB(DATABASE)
        db.get_every_entry()
    return render_template("open_database.html")

@auth.route("/create_database", methods=["GET", "POST"])
def sign_up():
    if request.method == "POST":
        DATABASE = request.form.get("DATABASE")
        masterKEY = request.form.get("masterKEY").encode()
        db = DB.DB(DATABASE)
        db.firstSetup()

    return render_template("create_database.html")
