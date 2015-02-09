# all the imports
import sqlite3
from flask import Flask, request, session, g, redirect, url_for, \
     abort, render_template, flash
from contextlib import closing

# configuration
DATABASE = '/tmp/films.db'
DEBUG = True
SECRET_KEY = 'RuJYsdKAgfFELaLajSRRrxZy'
USERNAME = 'admin'
PASSWORD = 'default'

# create our little application :)
app = Flask(__name__)
app.config.from_object(__name__)

# that way someone can set an environment variable called SFMOVIES_SETTINGS to specify a config file to be loaded which will then override the default values.
# the silent switch just tells Flask to not complain if no such environment key is set.
app.config.from_envvar('SFMOVIES_SETTINGS', silent=True)

def connect_db():
    return sqlite3.connect(app.config['DATABASE'])

def init_db():
    with closing(connect_db()) as db:
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()

@app.before_request
def before_request():
    g.db = connect_db()

@app.teardown_request
def teardown_request(exception):
    db = getattr(g, 'db', None)
    if db is not None:
        db.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)
