
from flask import Flask, jsonify, render_template, request
import app
from app.settings import *
#from jinja2 import Environment

@app.route('/_add_numbers')
def add_numbers():
    """Add two numbers server side, ridiculous but well..."""
    a = request.args.get('a', 0, type=int)
    b = request.args.get('b', 0, type=int)
    return jsonify(result=a + b)


@app.route('/')
def index():
    return render_template('index.html')



# env = Environment()
# print env.list_templates(extensions=None, filter_func=None)