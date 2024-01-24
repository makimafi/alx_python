"""
1-hbnb_route.py

A simple Flask web application with two routes.

- Route '/': Displays "Hello HBNB!"
- Route '/hbnb': Displays "HBNB"

Usage:
    Run this script to start the Flask web application.

    Example:
        python3 1-hbnb_route.py
"""

from flask import Flask

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Route to display 'Hello HBNB!'."""
    return 'Hello HBNB!'

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Route to display 'HBNB'."""
    return 'HBNB'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

