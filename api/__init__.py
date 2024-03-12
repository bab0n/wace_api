from flask import Flask
from flask_cors import CORS
from api.models.db import db
from config import Config


def create_app() -> Flask:
    app = Flask(__name__)
    app.config.from_object(Config)
    CORS(app)
    from api.api import api_blueprint

    db.init_app(app)
    app.register_blueprint(api_blueprint)

    return app


def create_db() -> None:
    app = create_app()
    with app.app_context():
        db.create_all()
