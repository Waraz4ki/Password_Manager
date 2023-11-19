from flask import Flask, render_template, abort
from flaskwebgui import FlaskUI
from Manager_App import create_app

app = create_app()

@app.errorhandler(401)
def unauthorized(error_code):
    print("401")
    return render_template("error_base.html", error = error_code)

@app.errorhandler(404)
def page_not_found(error_code):
    print("404")
    return render_template("error_base.html", error = error_code)

#TODO Find out if you can use tkinterer to display all the localhost stuff(html and css works I looked ut up)
if __name__ == '__main__':
    app.run(debug=True)
    #FlaskUI(app=app, server="flask").run()
