from flask import Flask, render_template
from flaskwebgui import FlaskUI
import psutil



app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("open_database.html")

@app.route("/cpu")
def cpu():
    return str(psutil.cpu_percent(interval=1))

if __name__ == '__main__':
    app.run(debug=True)
    #FlaskUI(app=app, server="flask").run()
