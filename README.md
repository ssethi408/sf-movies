# sf-movies
A service that shows on a map where movies have been filmed in San Francisco. 

The user should be able to filter the view using autocompletion search.

The data is available on <a href="http://www.datasf.org/">DataSF</a>:<a href="https://data.sfgov.org/Arts-Culture-and-Recreation-/Film-Locations-in-San-Francisco/yitu-d5am">Film Locations </a>

## Technical spec

The architecture will be split between a back-end and a web front-end, for instance providing a JSON in/out RESTful API. Feel free to use any other technologies provided that the general client/service architecture is respected.

Choose one of the following technical tracks that best suits your skillset:

- Full-stack: include both front-end and back-end.
- Back-end track: include a minimal front-end (e.g. a static view or API docs). Write, document and test your API as if it will be used by other services.
- Front-end track: include a minimal back-end, or use the data service directly. Focus on making the interface as polished as possible.

## Completion/Submission

- Full-stack track: Flask-based WSGI with a simple jQuery front-end with minimal CSS. 
- Due to a lack of time my submission does not contain the following:

1. TravisCI - wanted to fully automate testing and do assertions with a unit test framework called `unittest` that comes with Python. - Follow [these](http://flask.pocoo.org/docs/0.10/testing/) instructions and get it going.
1. Clean up the UI - CSS, JavaScript etc. - It doesn't look close to cleaned up.
1. Have the ability to allow for users to autocomplete/search for actors or directors or writers instead of just movies. We should output all the movies that they've been involved with to draw markers all over the map.
1. Markers and infoWindows for Locations should contain all information about the movie - not just the location (if available)
