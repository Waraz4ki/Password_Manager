from flask import Flask, render_template
from flaskwebgui import FlaskUI
from Manager_App import create_app
import tkinter
import customtkinter


app = create_app()

@app.errorhandler(404)
def page_not_found(error):
    return render_template("error_base.html")

#TODO Find out if you can use tkinterer to display all the localhost stuff(html and css works I looked ut up)
if __name__ == '__main__':
    app.run(debug=True)
    #FlaskUI(app=app, server="flask").run()
