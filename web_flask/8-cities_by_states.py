#!/usr/bin/python3
"""
script that starts a Flask web application
"""
from flask import Flask, render_template
from models import FileStorage


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/cities_by_states")
def number_odd_or_even_route():
        from models import storage
        from models.state import State
        from models.city import City
        sts = storage.all(State)
        cts = storage.all(City)
        return render_template("8-cities_by_states.html", sts=sts, cts=cts)


@app.teardown_appcontext
def teardown_db(exception):
        from models import storage
        storage.close()


if __name__ == '__main__':
        app.run(host=('0.0.0.0'),
                port=int('5000'), threaded=True)
