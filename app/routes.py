from flask import render_template, Request
from . import quotes_app


@quotes_app.route("/home")
def hello_world():
    return "<p>Hello, World!</p>"