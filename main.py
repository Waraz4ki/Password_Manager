import psutil

from flask import Flask, render_template
from UI_SERVER import create_app
from flaskwebgui import FlaskUI


app = create_app()


if __name__ == '__main__':
    app.run(debug=True)
    #FlaskUI(app=app, server="flask").run()
