# import secrets
# import string

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
        