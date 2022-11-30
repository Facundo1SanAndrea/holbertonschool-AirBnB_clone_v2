#!/usr/bin/python3
"""script that starts a Flask web application"""

from flask import Flask

app = Flask(__name__)


@app.route('/')
def index(strict_slashes=False):
    return "Hello HBNB!"


@app.route('/hbnb')
def hbnb(strict_slashes=False):
    return "HBNB"


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=5000)
