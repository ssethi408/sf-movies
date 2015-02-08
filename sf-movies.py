from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
import httplib
import ConfigParser
import io
app = Flask(__name__)

# Configuration parser needed to configure the database and other aspects of the application.
config = ConfigParser.RawConfigParser(allow_no_value=True)
config.readfp(io.BytesIO('../sf-movies.cfg')

# Get the Database Configuration and URI associated with it. If not found, set it to sqlite relative to the current path
# Want to configure more parts of the SQLALCHEMY? Here are some common configuration keys: https://pythonhosted.org/Flask-SQLAlchemy/config.html
if config.get("dbconfig", "uri") is None:
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////../sf-movies.db'
else
    app.config['SQLALCHEMY_DATABASE_URI'] = config.get("dbconfig", "uri")

# Create the SQLAlchemy database for your application
db = SQLAlchemy(app)

class Films(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150))
    release = db.Column(db.Integer)
    locations = db.Column(db.String(255))
    fun_facts = db.Column(db.String(255))
    production = db.Column(db.String(150))
    distributor = db.Column(db.String(150))
    director = db.Column(db.String(150))
    writer = db.Column(db.String(150))
    actor1 = db.Column(db.String(150))
    actor2 = db.Column(db.String(150))
    actor3 = db.Column(db.String(150))

    def __init__(self, title, release, locations, fun_facts, production, distributor, director, writer, actor1, actor2, actor3):
        self.title = title
        self.release = release
        self.locations = locations
        self.fun_facts = fun_facts
        self.production = production
        self.distributor = distributor
        self.director = director
        self.writer = writer
        self.actor1 = actor1
        self.actor2 = actor2
        self.actor3 = actor3

    def __repr__(self):
        return '<Title %r>' % self.title

@app.route('/')
def hello_world():
    return 'Hello World!'
##
@app.route('/movie-name/<movie>')
def movie_name(movie):
    ## Build a connection to call out to the 3rd party API
    conn = httplib.HTTPConnection("data.sfgov.org")
    ## Build the url string
    url = '/resource/yitu-d5am.json?title=%s' % movie
    ## Make the connection request
    conn.request("GET", url)
    r1 = conn.getresponse()
    if r1.status == 200:
        return r1.read()
##

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)
