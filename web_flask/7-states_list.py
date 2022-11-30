#!/usr/bin/python3
"""
Module 7-states_list.py
"""
from flask import Flask, render_template


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/states_list")
def number_odd_or_even_route():
        from models import storage
        from models.state import State
        sts = storage.all(State)
        return render_template("7-states_list.html", sts=sts)


@app.teardown_appcontext
def teardown_db(exception):
        from models import storage
        storage.close()


if __name__ == '__main__':
        app.run(host=('0.0.0.0'),
                port=int('5000'), threaded=True)