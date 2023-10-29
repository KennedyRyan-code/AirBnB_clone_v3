#!/usr/bin/python3
"""Flask Application"""
from flask import Flask, render_template, make_response, jsonify
from api.v1.views import app_views
from models import storage

app = Flask(__name__)

app.register_blueprint(app_views)

@app.teardown_appcontext
def close_db(error):
    """Closes the database on teardown."""
    storage.close()


@app.errorhandler(404)
def not_found(error):
    """ 404 Error
    ---
    responses:
      404:
        description: resource was not found
    """
    return make_response(jsonify({'error': "Not found"}), 404)

if __name__ == "__main__":
    host = os.getenv('HBNB_API_HOST', '0.0.0.0')
    port = int(os.getenv('HBNB_API_PORT', 5000))
    app.run(host=host, port=port, threaded=True)
