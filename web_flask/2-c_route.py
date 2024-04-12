#!/usr/bin/python3
from flask import Flask

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Route / display 'Hello HBNB!'"""
    return "Hello HBNB!"

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Route /hbnb display 'HBNB'"""
    return "HBNB"

@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """Route /c/<text> display 'C ' followed by the text, replace '_' with ' '"""
    formatted_text = text.replace('_', ' ')
    return f"C {formatted_text}"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)