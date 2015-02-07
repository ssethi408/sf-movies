from flask import Flask
import httplib
app = Flask(__name__)

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
