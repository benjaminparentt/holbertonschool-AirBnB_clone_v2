#!/usr/bin/python3
"""comment"""
from flask import Flask, render_template
from models import storage, State

app = Flask(__name__)

@app.route('/states', strict_slashes=False)
def states_list():
    """Display a HTML page with a list of all states."""
    states = list(storage.all(State).values())
    states.sort(key=lambda x: x.name)
    return render_template('9-states.html', states=states, id=None)

@app.route('/states/<id>', strict_slashes=False)
def states_detail(id):
    """Display a HTML page with details of a state and its cities."""
    state = storage.all(State).get('State.' + id)
    return render_template('9-states.html', states=[state] if state else [], id=id)

@app.teardown_appcontext
def close_session(exception):
    """Close the current SQLAlchemy session."""
    storage.close()

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
