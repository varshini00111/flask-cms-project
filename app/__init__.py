import logging
from flask import Flask

logging.basicConfig(level=logging.INFO)

def create_app():
    app = Flask(__name__)

    from app.views import main
    app.register_blueprint(main)

    return app
