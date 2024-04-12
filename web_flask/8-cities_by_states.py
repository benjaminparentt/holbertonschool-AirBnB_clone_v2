#!/usr/bin/python3
"""comment"""
from flask import Flask, render_template
from models import storage

app = Flask(__name__)

@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """Display a HTML page with a list of all states and cities."""
    states = list(storage.all("State").values())
    states.sort(key=lambda x: x.name)  # Sort states by name
    # Ensure cities are sorted as well if not inherently sorted by the relationship
    for state in states:
        state.cities.sort(key=lambda x: x.name)
    return render_template('8-cities_by_states.html', states=states)

@app.teardown_appcontext
def close_session(exception):
    """Close the current SQLAlchemy session."""
    storage.close()

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
