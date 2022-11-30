#!/usr/bin/python3
"""
script that starts a Flask web application
"""
from flask import Flask, render_template


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/states")
def states_route():
        from models import storage
        from models.state import State
        sts = storage.all(State)
        return render_template("9-states.html", sts=sts)


@app.route("/states/<id>")
def state_with_id(id):
        from models import storage
        from models.state import State
        from models.city import City
        cts = storage.all(City)
        sts = storage.all(State)
        for i in sts.values():
                st = False
                if i.id == id:
                        st = i.name
                        break

        return render_template("9-states.html",
                               sts=sts, cts=cts, st_id=id, st=st)


@app.teardown_appcontext
def teardown_db(exception):
        from models import storage
        storage.close()


if __name__ == '__main__':
        app.run(host=('0.0.0.0'),
                port=int('5000'), threaded=True)