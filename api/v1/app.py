#!/usr/bin/python3
# app.py

"""Flask server (variable app)
"""


from flask import Flask, jsonify, make_response
from models import storage
from api.v1.views import app_views
from os import getenv
from flask_cors import CORS
from flasgger import Swagger

app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
app.register_blueprint(app_views)
cors = CORS(app, resources={r"/api/*": {"origins": "0.0.0.0"}})
app.url_map.strict_slashes = False


@app.teardown_appcontext
def downtear(self):
    '''Status of your API'''
    storage.close()


@app.errorhandler(404)
def page_not_found(error):
    '''return render_template'''
    return jsonify({"error": "Not found"}), 404


app.config['SWAGGER'] = {
    'title': 'AirBnB clone - RESTful API',
    'description': 'The api created for the hbnb restful api project,\
    all the documentation will be shown below',
    'uiversion': 3}

Swagger(app)


if __name__ == "__main__":
    host = getenv('HBNB_API_HOST')
    port = getenv('HBNB_API_PORT')
    if not host:
        host = '0.0.0.0'
    if not port:
        port = '5000'
    app.run(host=host, port=port, threaded=True)
