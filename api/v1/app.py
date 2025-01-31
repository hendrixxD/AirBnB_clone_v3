#!/usr/bin/python3
"""
Flask App that integrates with AirBnB static HTML Template
"""

from flask import Flask
from models import storage
from api.v1.views import app_views
from os import getenv
from flask_cors import CORS

app = Flask(__name__)
app.register_blueprint(app_views)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
CORS(app, resources={r"/*": {"origins": "0.0.0.0"}})


@app.teardown_appcontext
def tear_down(error):
    """
    closes alchemy session
    """
    storage.close()


@app.errorhandler(404)
def error():
    """
    an eror handler for json
    """
    return jsonify({"error": "Not found"}), 404


if __name__ == '__main__':
    app.run(host=getenv('HBNB_API_HOST'),
            port=getenv('HBNB_API_PORT'),
            threaded=True)
