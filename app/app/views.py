from app import app
from flask import render_template, request

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/404")
def not_found():
    return render_template("404.html")
