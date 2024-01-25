#!/usr/bin/python3
""" Starts a Flask web application """

from flask import Flask

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello_hbnb():
    """ Display 'Hello HBNB!' """
    return 'Hello HBNB!'


@app.route('/hbnb')
def hbnb():
    """ Display 'HBNB' """
    return 'HBNB'


@app.route('/c/<text>')
def c_text(text):
    """ Display 'C ', followed by the value of the text variable """
    return 'C {}'.format(text.replace('_', ' '))


@app.route('/python/<text>')
def python_text(text='is_cool'):
    """ Display 'Python ', followed by the value of the text variable """
    return 'Python {}'.format(text.replace('_', ' '))


@app.route('/number/<int:n>')
def is_number(n):
    """ Display 'n is a number' only if n is an integer """
    return '{} is a number'.format(n)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
