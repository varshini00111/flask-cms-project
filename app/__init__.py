from flask import Flask
import logging

def create_app():
    app = Flask(__name__)

    # Logging setup
    logging.basicConfig(level=logging.INFO)

    from .views import main
    app.register_blueprint(main)

    return app
