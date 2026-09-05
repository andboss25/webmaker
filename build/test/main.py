
import flask
#% IMPORTS_GO_HERE %#

App = flask.Flask(
    "test"
)

#% CLASSES_GO_HERE %#
#% ROUTES_GO_HERE %#

App.run('0.0.0.0',80)