#!/usr/bin/python3
"""
script that starts a Flask web application
"""
from flask import Flask, render_template


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/hbnb_filters")
def hbnb_filters_route():
        from models.amenity import Amenity
        from models.state import State
        from models.city import City
        from models import storage
        cts = storage.all(City)
        sts = storage.all(State)
        ats = storage.all(Amenity)
        return render_template("10-hbnb_filters.html", cts=cts, sts=sts, ats=ats)


@app.teardown_appcontext
def teardown_db(exception):
        from models import storage
        storage.close()


if __name__ == '__main__':
        app.run(host=('0.0.0.0'),
                port=int('5000'), threaded=True, debug=False)