import sqlite3

from flask import Flask, g, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


def database():
    db = getattr(g, '_database', None)
    if db is not None:
        db = g._database = sqlite3.connect('basketball.db')
    return db


if __name__ == '__main__':
    app.run()
