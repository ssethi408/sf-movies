# all the imports
import sqlite3
import json
import urllib
import httplib
from flask import Flask, request, session, g, redirect, url_for, \
     abort, render_template, flash, jsonify
from contextlib import closing

# configuration
DATABASE = '/tmp/films.db'
DEBUG = True
SECRET_KEY = 'RuJYsdKAgfFELaLajSRRrxZy'
USERNAME = 'admin'
PASSWORD = 'default'

# create application
app = Flask(__name__)
app.config.from_object(__name__)

# that way someone can set an environment variable called SFMOVIES_SETTINGS to specify a config file to be loaded which will then override the default values.
# the silent switch just tells Flask to not complain if no such environment key is set.
app.config.from_envvar('SFMOVIES_SETTINGS', silent=True)

# DB Connection, initiatialization and querying functions
def connect_db():
    return sqlite3.connect(app.config['DATABASE'])

def init_db():
    with closing(connect_db()) as db:
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = connect_db()
    return db

def query_db(query, args=(), one=False):
    cur = get_db().execute(query, args)
    rv = cur.fetchall()
    cur.close()
    return (rv[0] if rv else None) if one else rv

@app.before_request
def before_request():
    g.db = connect_db()

@app.teardown_request
def teardown_request(exception):
    db = getattr(g, 'db', None)
    if db is not None:
        db.close()

@app.route('/')
def welcome():
    return render_template('welcome.html')

#Return a list of movies based on what's being searched for Autocomplete
@app.route('/_movie-name')
def xhr_movie_name():
    movie_request = request.args.get('movie', 0)
    entries = [dict(value=title[0]) for title in query_db("select distinct(title) from films where title like '%s%%'" % movie_request)]
    return json.dumps(entries)
    
#Return a list of movies based on what's being searched
@app.route('/db-movie-name/<path:movie>')
def movie_name(movie):
    decoded_movie = urllib.unquote(movie)
    #entries = [dict(label=movie, value=title[0]) for title in query_db("select distinct(title) from films where title like '%s%%'" % decoded_movie)]
    entries = [dict(movies=title[0]) for title in query_db("select distinct(title) from films where title like '%s%%'" % decoded_movie)]
    return json.dumps(entries)

#Return a list of locations for the movie searched
@app.route('/locations/<path:movie>')
def locations(movie):
    decoded_movie = urllib.unquote(movie)
    entries = [dict(locations=title[3]) for title in query_db("select * from films where title = '%s'" % decoded_movie)]
    return json.dumps(entries)

@app.route('/movie-name-api/<movie>')
def movie_name_api(movie):
    ## Build a connection to call out to the 3rd party API
    conn = httplib.HTTPConnection("data.sfgov.org")
    ## Build the url string
    url = '/resource/yitu-d5am.json?title=%s' % movie
    ## Make the connection request
    conn.request("GET", url)
    r1 = conn.getresponse()
    if r1.status == 200:
        return r1.read()

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)
