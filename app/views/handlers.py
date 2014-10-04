from flask import render_template
from app import app

@app.errorhandler(404)
def page_not_found(e):
    return render_template("stuff/error404.html")


@app.errorhandler(500)
def page_not_found(e):
    return render_template("stuff/error500.html")

