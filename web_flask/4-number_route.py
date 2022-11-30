#!/usr/bin/python3
"""script that starts a Flask web application"""

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_is_fun(text):
    return "C " + text.replace('_', ' ')


@app.route('/python', defaults={'text': "is cool"}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_is_cool(text="is cool"):
    return "Python " + text.replace('_', ' ')


@app.route('/number/<int:n>', strict_slashes=False)
def is_number(n):
    return "{} is a number".format(n)


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=5000)
