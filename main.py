from flask import Flask, render_template
from Manager_App import create_app
from flaskwebgui import FlaskUI, find_browser
import json
app = create_app()

@app.errorhandler(404)
def page_not_found(error):
    return render_template("error_base.html")

if __name__ == '__main__':
    app.run(debug=True)
    #FlaskUI(app=app, server="flask").run()
